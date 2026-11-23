#!/usr/bin/env bash
# Adds vetted upstreams as submodules. Usage: add-upstreams.sh [name ...]  (default: all)
# Refuses repos not marked REMOTE-VERIFIED-BY-TEAM unless ALLOW_UNVERIFIED=1.
# Prefer the hardened procedure in documentation/CLONE_SEQUENCE.md. Does NOT run any upstream code. Review SECURITY_REVIEW.md before adding.
set -euo pipefail; cd "$(dirname "$0")/.."
[ -d .git ] || git init -q
want=" $* "
grep -v '^#' scripts/repos.txt | while IFS='|' read -r n u c st; do
  [ -n "$n" ] || continue
  [ "$#" -eq 0 ] || [[ "$want" == *" $n "* ]] || continue
  if [ "$st" = "RESTRICTED-LICENCE" ] && [ "${ALLOW_RESTRICTED:-0}" != "1" ]; then echo "skip $n (restricted licence: LINK-ONLY; ALLOW_RESTRICTED=1 only after reading its LICENSE)"; continue; fi
  if [ "$st" != "REMOTE-VERIFIED-BY-TEAM" ] && [ "${ALLOW_UNVERIFIED:-0}" != "1" ]; then echo "skip $n ($st; set ALLOW_UNVERIFIED=1 to override)"; continue; fi
  [ -e "upstream/$n" ] && { echo "skip $n (exists)"; continue; }
  echo "adding $n"; git submodule add "$u" "upstream/$n" || echo "FAILED $n" >&2
done
