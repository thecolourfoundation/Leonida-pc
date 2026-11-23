#!/usr/bin/env bash
set -euo pipefail; cd "$(dirname "$0")/.."
git submodule status --recursive
git submodule foreach --quiet 'git fsck --no-progress >/dev/null 2>&1 && echo "$name: fsck ok" || echo "$name: FSCK PROBLEM"'
git submodule foreach --quiet 'git diff --quiet && git diff --cached --quiet && echo "$name: clean" || echo "$name: MODIFIED (upstream must stay pristine)"'
