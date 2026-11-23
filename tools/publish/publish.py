#!/usr/bin/env python3
"""Publish this repository to GitHub with a token taken from the GH_TOKEN environment variable.
The token is never printed, never written to .git/config, never put in a URL or argv. Stdlib only."""
import argparse, base64, json, os, subprocess, sys, urllib.error, urllib.request

API = 'https://api.github.com'
DEFAULT_NAME = 'Leonida-PC'
DEFAULT_DESC = 'Leonida PC: upstream vetting, licence tooling and tests. GTA VI does not boot; no game files included.'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def scrub(text, token):
    return text.replace(token, '***') if token else text


def noreply_email(login, uid):
    return f'{uid}+{login}@users.noreply.github.com'


def api_request(method, path, token, body=None, base=API):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(base + path, data=data, method=method, headers={
        'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'leonida-pc-publish', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, dict(r.headers), json.loads(r.read() or b'null')
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read() or b'null')
        except ValueError:
            payload = None
        return e.code, dict(e.headers), payload


def whoami(token, base=API):
    st, hdr, j = api_request('GET', '/user', token, base=base)
    if st != 200:
        raise RuntimeError(f'authentication failed: HTTP {st}')
    return j['login'], j['id'], hdr.get('X-OAuth-Scopes', '(fine-grained token or none)')


def repo_status(token, owner, name, base=API):
    return api_request('GET', f'/repos/{owner}/{name}', token, base=base)[0]


def ensure_repo(token, owner, name, login, private=False, create=True, base=API):
    st, _, j = api_request('GET', f'/repos/{owner}/{name}', token, base=base)
    if st == 200:
        return j, False
    if st != 404:
        raise RuntimeError(f'could not look up {owner}/{name}: HTTP {st}')
    if not create:
        raise RuntimeError(f'{owner}/{name} does not exist; create it in the web UI or drop --no-create')
    path = '/user/repos' if owner.lower() == login.lower() else f'/orgs/{owner}/repos'
    st, _, j = api_request('POST', path, token, {'name': name, 'description': DEFAULT_DESC, 'private': private,
                                                  'has_issues': True, 'auto_init': False}, base=base)
    if st != 201:
        raise RuntimeError(f'create failed: HTTP {st}: {j.get("message") if isinstance(j, dict) else j}')
    return j, True


def run(args, cwd, env=None):
    p = subprocess.run(['git'] + args, cwd=cwd, env=env, capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f'git {" ".join(args[:2])} failed: {p.stderr.strip() or p.stdout.strip()}')
    return p.stdout


def rewrite_identity(repo, name, email):
    """Rewrite every commit's author/committer to name/email and recreate tags on the rewritten commits."""
    saved = []
    for t in run(['tag'], repo).split():
        typ = run(['cat-file', '-t', t], repo).strip()
        msg = run(['tag', '-l', '--format=%(contents)', t], repo).strip()
        subj = run(['log', '-1', '--format=%s', t + '^{commit}'], repo).strip()
        saved.append((t, typ, msg, subj))
    run(['config', 'user.name', name], repo)
    run(['config', 'user.email', email], repo)
    env = dict(os.environ, GIT_SEQUENCE_EDITOR='true', GIT_EDITOR='true')
    run(['rebase', '-r', '--root', '--exec', 'git commit --amend --reset-author --no-edit'], repo, env)
    by_subject = {}
    for line in run(['log', '--format=%H%x09%s'], repo).splitlines():
        h, s = line.split('\t', 1)
        by_subject.setdefault(s, h)
    for t, typ, msg, subj in saved:
        run(['tag', '-d', t], repo)
        if typ == 'tag':
            run(['tag', '-a', t, '-m', msg, by_subject[subj]], repo)
        else:
            run(['tag', t, by_subject[subj]], repo)


def push(repo, url, token, branch='main'):
    """Push branch and tags by URL (no remote is written, token only in the process environment)."""
    hdr = 'AUTHORIZATION: basic ' + base64.b64encode(f'x-access-token:{token}'.encode()).decode()
    env = dict(os.environ, GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='http.extraheader',
               GIT_CONFIG_VALUE_0=hdr, GIT_TERMINAL_PROMPT='0')
    run(['push', url, f'{branch}:{branch}', '--tags'], repo, env)
    if 'origin' not in run(['remote'], repo).split():
        run(['remote', 'add', 'origin', url], repo)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--owner'); ap.add_argument('--name', default=DEFAULT_NAME)
    ap.add_argument('--private', action='store_true'); ap.add_argument('--no-create', action='store_true')
    ap.add_argument('--rewrite-identity', action='store_true', help='replace placeholder author with your GitHub noreply identity')
    ap.add_argument('--skip-check', action='store_true', help='skip the pre-push `make check`')
    ap.add_argument('--whoami', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--yes', action='store_true', help='actually publish')
    ap.add_argument('--repo-dir', default=ROOT)
    ap.add_argument('--api-base', default=API, help='testing only'); ap.add_argument('--remote-url', help='testing only')
    a = ap.parse_args(argv)
    token = os.environ.get('GH_TOKEN', '').strip()
    if not token:
        print('Set GH_TOKEN in the environment (Colab Secrets or getpass). Never paste a token into chat or a file.', file=sys.stderr)
        return 2
    try:
        login, uid, scopes = whoami(token, a.api_base)
        print(f'authenticated as {login} (scopes: {scopes})')
        if a.whoami:
            return 0
        owner = a.owner or login
        if not a.skip_check:
            if subprocess.run(['make', 'check'], cwd=a.repo_dir).returncode:
                print('make check failed: not publishing', file=sys.stderr)
                return 3
        if a.dry_run:
            st = repo_status(token, owner, a.name, a.api_base)
            print(f'DRY RUN: {owner}/{a.name} ' + ('exists' if st == 200 else 'does not exist; would be created' if st == 404 else f'lookup HTTP {st}'))
            if a.rewrite_identity:
                print(f'DRY RUN: would rewrite authors to {login} <{noreply_email(login, uid)}>')
            return 0
        if not a.yes:
            print('Add --yes to publish (use --dry-run first).')
            return 1
        _, created = ensure_repo(token, owner, a.name, login, a.private, not a.no_create, a.api_base)
        print('created repo' if created else 'repo already exists')
        if a.rewrite_identity:
            rewrite_identity(a.repo_dir, login, noreply_email(login, uid))
            print('rewrote commit identity and re-created tags')
        url = a.remote_url or f'https://github.com/{owner}/{a.name}.git'
        push(a.repo_dir, url, token)
        print(f'pushed: https://github.com/{owner}/{a.name}')
        return 0
    except RuntimeError as e:
        print(scrub(str(e), token), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
