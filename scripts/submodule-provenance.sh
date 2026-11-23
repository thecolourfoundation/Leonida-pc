#!/usr/bin/env bash
# Passive: lists gitlinks (pinned submodule commits) and .gitmodules URLs per upstream clone; flags non-github.com hosts.
# No network, no submodule init, runs nothing from upstream.  Usage: submodule-provenance.sh [upstream/<name> ...] -> reports/submodules-<name>.txt
set -uo pipefail; cd "$(dirname "$0")/.."
targets=("$@"); [ ${#targets[@]} -gt 0 ] || targets=(upstream/*/)
for t in "${targets[@]}"; do [ -e "$t/.git" ] || continue; n=$(basename "$t"); out=reports/submodules-$n.txt
{ echo "## gitlinks at HEAD (path -> pinned commit)"; git -C "$t" ls-tree -r HEAD | awk '$2=="commit"{print $4" -> "$3}'
  echo "## .gitmodules at HEAD"; git -C "$t" show HEAD:.gitmodules 2>/dev/null || echo "(none)"
  echo "## submodule URLs not on github.com"; git -C "$t" show HEAD:.gitmodules 2>/dev/null | grep -E 'url *=' | grep -v 'github.com' || echo "(none)"
} > "$out" 2>&1; echo "wrote $out"; done
