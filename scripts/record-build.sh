#!/usr/bin/env bash
# Usage: record-build.sh <repo> -- <command...>   Appends command/env/exit code to BUILD_LOG.md
# Run only inside an isolated VM/container, after SECURITY_REVIEW sign-off.
set -uo pipefail; cd "$(dirname "$0")/.."; r=$1; shift; [ "${1:-}" = "--" ] && shift
log=$(mktemp); ( cd "upstream/$r" && "$@" ) >"$log" 2>&1; ec=$?
{ echo; echo "### $(date -u +%FT%TZ) - $r"; echo "- command: \`$*\`"; echo "- env: $(uname -srm); $(gcc --version 2>/dev/null|head -1)"
  echo "- upstream sha: $(git -C upstream/$r rev-parse HEAD)"; echo "- exit code: $ec"; echo '```'; tail -40 "$log"; echo '```'; } >> BUILD_LOG.md
exit $ec
