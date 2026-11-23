#!/usr/bin/env bash
# Emits markdown table from repos.txt + licence-matrix.csv + local clones. Local columns reflect only what is actually cloned here.
set -euo pipefail; cd "$(dirname "$0")/.."
echo "| Repo | Category | URL | Remote status | Licence (reported) | Cloned locally | Local SHA | Licence file |"; echo "|---|---|---|---|---|---|---|---|"
grep -v '^#' scripts/repos.txt | while IFS='|' read -r n u c st; do
  [ -n "$n" ] || continue
  lr=$(awk -F, -v n="$n" '$1==n{print $2}' reports/licence-matrix.csv); lr=${lr:-UNKNOWN}
  if [ -e "upstream/$n/.git" ]; then sha=$(git -C upstream/$n rev-parse --short HEAD)
    lic=$(find upstream/$n -maxdepth 1 -iname 'licen[sc]e*' | head -1); cl=yes
  else sha=-; lic=-; cl=NO; fi
  echo "| $n | $c | $u | $st | $lr | $cl | $sha | ${lic:-NONE} |"
done
