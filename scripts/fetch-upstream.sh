#!/usr/bin/env bash
# One-command hardened fetch of the official Leonida upstream + identity report.
# No checkout, hooks disabled, no submodule init: nothing from upstream is executed.
set -euo pipefail; cd "$(dirname "$0")/.."
url=${UPSTREAM_URL:-https://github.com/ItsNotRexed/Leonida.git}
case $url in https://github.com/*) ;; *) [ "${ALLOW_TEST_URL:-0}" = 1 ] || { echo "refusing non-github URL: $url" >&2; exit 2; };; esac
dest=upstream/Leonida
[ ! -e "$dest" ] || { echo "$dest already exists; remove it or use scripts/update-upstreams.sh" >&2; exit 3; }
GIT_LFS_SKIP_SMUDGE=1 git clone --no-checkout --no-recurse-submodules -c core.hooksPath=/dev/null "$url" "$dest" || { echo "clone failed (is github.com reachable? run: make doctor)" >&2; exit 4; }
mkdir -p reports; out=reports/upstream-identity.txt
{ echo "# Leonida identity, read from the clone before checkout ($(date -u +%FT%TZ))"
  echo "url: $url"; echo "sha: $(git -C $dest rev-parse HEAD)"; echo "branch: $(git -C $dest rev-parse --abbrev-ref HEAD)"
  echo "date: $(git -C $dest log -1 --format=%cI)"; echo "tags: $(git -C $dest tag | tail -5 | tr '\n' ' ')"
  echo "## gitlinks (submodule pins)"; git -C $dest ls-tree -r HEAD | awk '$2=="commit"{print $4" -> "$3}'
  echo "## .gitmodules"; git -C $dest show HEAD:.gitmodules 2>/dev/null || echo "(none)"
  echo "## LICENSE (first 15 lines)"; git -C $dest show HEAD:LICENSE 2>/dev/null | head -15 || true
  echo "## build/doc files"; git -C $dest ls-tree -r --name-only HEAD | grep -iE 'readme|build|install|\.github/workflows|requirements|\.csproj|CMakeLists' | head -60 || true
} > "$out"
cat "$out"; echo; echo "Saved to $out. Paste it into an issue/PR. Read the build scripts BEFORE any checkout or build."
