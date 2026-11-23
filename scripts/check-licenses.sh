#!/usr/bin/env bash
# Lists licence files per upstream; flags repos with none. Does not judge compatibility.
set -euo pipefail; cd "$(dirname "$0")/.."
for d in upstream/*/; do [ -d "$d" ] || continue; n=$(basename "$d")
  f=$(find "$d" -maxdepth 2 -iregex '.*/\(licen[sc]e\|copying\|notice\)[^/]*' -not -path '*/.git/*' | head -5)
  if [ -n "$f" ]; then echo "== $n"; echo "$f"; else echo "== $n: NO LICENCE FILE (all rights reserved by default; do not redistribute)"; fi
done
