"""Offline tests for tools/publish/publish.py: stub GitHub API on localhost, local bare repo as the remote."""
import contextlib, http.server, importlib.util, io, json, os, subprocess, tempfile, threading, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('publish', os.path.join(ROOT, 'tools', 'publish', 'publish.py'))
pub = importlib.util.module_from_spec(spec); spec.loader.exec_module(pub)
TOKEN = 'tok_' + 'x' * 24
ENV = dict(os.environ, GIT_AUTHOR_NAME='old', GIT_AUTHOR_EMAIL='old@local', GIT_COMMITTER_NAME='old', GIT_COMMITTER_EMAIL='old@local')


class Stub(http.server.BaseHTTPRequestHandler):
    created, seen_auth = set(), []

    def log_message(self, *a): pass

    def _send(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code); self.send_header('Content-Type', 'application/json')
        self.send_header('X-OAuth-Scopes', 'repo'); self.send_header('Content-Length', str(len(data)))
        self.end_headers(); self.wfile.write(data)

    def do_GET(self):
        Stub.seen_auth.append(self.headers.get('Authorization'))
        if self.headers.get('Authorization') != 'Bearer ' + TOKEN: return self._send(401, {'message': 'Bad credentials'})
        if self.path == '/user': return self._send(200, {'login': 'tester', 'id': 42})
        p = self.path.split('/', 2)[2]
        self._send(200 if p in Stub.created else 404, {'full_name': p})

    def do_POST(self):
        Stub.seen_auth.append(self.headers.get('Authorization'))
        body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        owner = 'tester' if self.path == '/user/repos' else self.path.split('/')[2]
        Stub.created.add(f"{owner}/{body['name']}"); self._send(201, {'full_name': f"{owner}/{body['name']}"})


def git(cwd, *a, env=ENV):
    return subprocess.run(['git', *a], cwd=cwd, env=env, capture_output=True, text=True, check=True).stdout


def make_repo(d):
    git(d, 'init', '-q', '-b', 'main')
    for s in ('first', 'second', 'Release docs'):
        with open(os.path.join(d, 'f'), 'a') as fh:
            fh.write(s + '\n')
        git(d, 'add', '-A'); git(d, 'commit', '-qm', s)
    git(d, 'tag', '-a', 'v1', '-m', 'release candidate msg', 'HEAD')


class Publish(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = http.server.HTTPServer(('127.0.0.1', 0), Stub)
        cls.base = f'http://127.0.0.1:{cls.srv.server_port}'
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls): cls.srv.shutdown(); cls.srv.server_close()

    def setUp(self): Stub.created.clear()

    def test_helpers(self):
        self.assertEqual(pub.noreply_email('bob', 7), '7+bob@users.noreply.github.com')
        self.assertEqual(pub.scrub('a ' + TOKEN + ' b', TOKEN), 'a *** b')

    def test_whoami_and_bad_token(self):
        self.assertEqual(pub.whoami(TOKEN, self.base)[:2], ('tester', 42))
        with self.assertRaises(RuntimeError): pub.whoami('wrong', self.base)

    def test_ensure_repo_user_and_org_and_nocreate(self):
        _, created = pub.ensure_repo(TOKEN, 'tester', 'Leonida-PC', 'tester', base=self.base); self.assertTrue(created)
        _, created = pub.ensure_repo(TOKEN, 'tester', 'Leonida-PC', 'tester', base=self.base); self.assertFalse(created)
        _, created = pub.ensure_repo(TOKEN, 'someorg', 'Leonida-PC', 'tester', base=self.base); self.assertTrue(created)
        self.assertIn('someorg/Leonida-PC', Stub.created)
        with self.assertRaises(RuntimeError): pub.ensure_repo(TOKEN, 'tester', 'nope', 'tester', create=False, base=self.base)

    def test_rewrite_identity_keeps_tree_and_moves_tag(self):
        with tempfile.TemporaryDirectory() as d:
            make_repo(d); tree = git(d, 'rev-parse', 'HEAD^{tree}'); old_tag_target = git(d, 'rev-parse', 'v1^{commit}')
            pub.rewrite_identity(d, 'tester', pub.noreply_email('tester', 42))
            self.assertEqual(git(d, 'rev-parse', 'HEAD^{tree}'), tree)
            self.assertEqual(set(git(d, 'log', '--format=%an|%ae|%cn').split()), {'tester|42+tester@users.noreply.github.com|tester'})
            self.assertEqual(git(d, 'cat-file', '-t', 'v1').strip(), 'tag')
            self.assertEqual(git(d, 'log', '-1', '--format=%s', 'v1^{commit}').strip(), 'Release docs')
            self.assertNotEqual(git(d, 'rev-parse', 'v1^{commit}'), old_tag_target)
            self.assertEqual(git(d, 'tag', '-l', '--format=%(contents)', 'v1').strip(), 'release candidate msg')

    def test_push_by_url_leaves_no_token_in_config(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as bare:
            make_repo(d); git(bare, 'init', '-q', '--bare')
            pub.push(d, bare, TOKEN)
            self.assertIn('main', git(bare, 'branch').split()); self.assertIn('v1', git(bare, 'tag').split())
            with open(os.path.join(d, '.git', 'config')) as fh:
                cfg = fh.read()
            self.assertNotIn(TOKEN, cfg); self.assertNotIn('x-access-token', cfg)

    def test_end_to_end_cli(self):
        os.environ['GH_TOKEN'] = TOKEN
        try:
            with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as bare:
                make_repo(d); git(bare, 'init', '-q', '--bare')
                common = ['--repo-dir', d, '--skip-check', '--api-base', self.base, '--remote-url', bare]
                out = io.StringIO()
                with contextlib.redirect_stdout(out): rc = pub.main(common + ['--dry-run', '--rewrite-identity'])
                self.assertEqual(rc, 0); self.assertIn('would be created', out.getvalue()); self.assertEqual(Stub.created, set())
                with contextlib.redirect_stdout(out): rc = pub.main(common)
                self.assertEqual(rc, 1); self.assertEqual(Stub.created, set())  # refuses without --yes
                out = io.StringIO()
                with contextlib.redirect_stdout(out): rc = pub.main(common + ['--yes', '--rewrite-identity'])
                self.assertEqual(rc, 0); self.assertIn('tester/Leonida-PC', Stub.created)
                self.assertIn('v1', git(bare, 'tag').split())
                self.assertNotIn(TOKEN, out.getvalue())
                self.assertEqual(git(bare, 'log', '-1', '--format=%an', 'main').strip(), 'tester')
        finally:
            del os.environ['GH_TOKEN']

    def test_requires_token(self):
        os.environ.pop('GH_TOKEN', None)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(pub.main(['--whoami']), 2)


if __name__ == '__main__':
    unittest.main()
