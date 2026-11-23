#!/usr/bin/env bash
# Emits markdown table from repos.txt + cloned repos. Facts only from the clones.
set -euo pipefail; cd "$(dirname "$0")/.."
echo "| Repo | URL | Cloned | SHA | Licence file | Status |"; echo "|---|---|---|---|---|---|"
grep -v '^#' scripts/repos.txt | while IFS='|' read -r n u c; do
  if [ -e "upstream/$n/.git" ]; then sha=$(git -C upstream/$n rev-parse --short HEAD)
    lic=$(find upstream/$n -maxdepth 1 -iname 'licen[sc]e*' | head -1); cl=yes
  else sha=-; lic=-; cl=NO; fi
  echo "| $n | $u | $cl | $sha | ${lic:-NONE} | UNVERIFIED |"
done
