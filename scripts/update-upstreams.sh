#!/usr/bin/env bash
set -euo pipefail; cd "$(dirname "$0")/.."
git submodule update --init --remote --no-recurse-submodules
./scripts/record-commits.sh
