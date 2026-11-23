# Publishing (not done: no GitHub access or credentials here)
```
cd Leonida-PC
git log --oneline && git tag               # main branch, tag v0.1.0-rc1
gh auth status                             # confirm account and org permissions first; never paste tokens anywhere
gh repo create <OWNER>/Leonida-PC --public --source=. --remote=origin \
  --description "Leonida PC research workspace: upstream vetting, licence tooling, tests" --push
git push origin --tags
# without gh: create an empty repo in the web UI, then
git remote add origin git@github.com:<OWNER>/Leonida-PC.git
git push -u origin main --follow-tags
```
Before pushing: confirm the LICENSE choice for original files, and set your author identity (`git config user.name/email`; existing commits use a placeholder `ws@local`; rewrite with `git rebase -r --root --exec 'git commit --amend --reset-author --no-edit'` if wanted). After pushing: check the Actions tab, then pin action versions to commit SHAs.

## Colab
tools/colab/leonida_bringup.ipynb: hardened clone + provenance + scans + Linux staged builds. UNTESTED (not run in Colab). Cannot boot the game: no Windows, no display, limited disk.

## Publish from Colab with your own token (recommended path)
Open tools/colab/publish_to_github.ipynb in Colab, store the token as the Colab secret `GH_TOKEN`, run dry-run, then the real publish. The helper (tools/publish/publish.py) is tested offline against a stub API and a local bare repo; it has not been run against real GitHub. It never prints the token or writes it to disk or `.git/config`. Repo name: `Leonida-PC`.
