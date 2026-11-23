#!/usr/bin/env bash
# Records exact upstream commit SHA/date/remote to reports/upstream-commits.tsv
set -euo pipefail; cd "$(dirname "$0")/.."
out=reports/upstream-commits.tsv; printf "name\tremote\tsha\tdate\ttag\n" > $out
for d in upstream/*/; do [ -e "$d/.git" ] || continue
  n=$(basename "$d")
  printf "%s\t%s\t%s\t%s\t%s\n" "$n" "$(git -C $d remote get-url origin)" "$(git -C $d rev-parse HEAD)" \
    "$(git -C $d log -1 --format=%cI)" "$(git -C $d describe --tags --always 2>/dev/null)" >> $out
done; cat $out
