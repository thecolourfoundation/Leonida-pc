#!/usr/bin/env bash
# Emits markdown table from repos.txt + local clones. Local columns reflect only what is actually cloned here.
set -euo pipefail; cd "$(dirname "$0")/.."
echo "| Repo | Category | URL | Remote status | Cloned locally | Local SHA | Licence file |"; echo "|---|---|---|---|---|---|---|"
grep -v '^#' scripts/repos.txt | while IFS='|' read -r n u c st; do
  [ -n "$n" ] || continue
  if [ -e "upstream/$n/.git" ]; then sha=$(git -C upstream/$n rev-parse --short HEAD)
    lic=$(find upstream/$n -maxdepth 1 -iname 'licen[sc]e*' | head -1); cl=yes
  else sha=-; lic=-; cl=NO; fi
  echo "| $n | $c | $u | $st | $cl | $sha | ${lic:-NONE} |"
done
