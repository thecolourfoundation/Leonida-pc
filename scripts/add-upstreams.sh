#!/usr/bin/env bash
# Adds vetted upstreams as submodules. Usage: add-upstreams.sh [name ...]  (default: all)
# Does NOT run any upstream code. Review SECURITY_REVIEW.md before adding.
set -euo pipefail; cd "$(dirname "$0")/.."
[ -d .git ] || git init -q
want=" $* "
grep -v '^#' scripts/repos.txt | while IFS='|' read -r n u c; do
  [ -n "$n" ] || continue
  [ "$#" -eq 0 ] || [[ "$want" == *" $n "* ]] || continue
  [ -e "upstream/$n" ] && { echo "skip $n (exists)"; continue; }
  echo "adding $n"; git submodule add "$u" "upstream/$n" || echo "FAILED $n" >&2
done
