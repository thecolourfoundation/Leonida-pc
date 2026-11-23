# Publishing (not done: no GitHub access or credentials here)
```
cd Leonida-PC-Research
git log --oneline && git tag               # main branch, tag v0.1.0-rc1
gh auth status                             # confirm account and org permissions first; never paste tokens anywhere
gh repo create <OWNER>/Leonida-PC-Research --public --source=. --remote=origin \
  --description "Leonida PC research workspace: upstream vetting, licence tooling, tests" --push
git push origin --tags
# without gh: create an empty repo in the web UI, then
git remote add origin git@github.com:<OWNER>/Leonida-PC-Research.git
git push -u origin main --follow-tags
```
Before pushing: confirm the LICENSE choice for original files, and set your author identity (`git config user.name/email`; existing commits use a placeholder `ws@local`; rewrite with `git rebase -r --root --exec 'git commit --amend --reset-author --no-edit'` if wanted). After pushing: check the Actions tab, then pin action versions to commit SHAs.

## Colab
tools/colab/leonida_bringup.ipynb: hardened clone + provenance + scans + Linux staged builds. UNTESTED (not run in Colab). Cannot boot the game: no Windows, no display, limited disk.
