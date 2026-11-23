#!/usr/bin/env bash
# Environment check for contributors. Read-only. Exit 1 only if git/python3/make are missing.
cd "$(dirname "$0")/.." || exit 1
need=0
chk(){ if command -v "$1" >/dev/null 2>&1; then printf '  [ok]      %-10s %s\n' "$1" "$("$1" --version 2>&1 | head -1)"; else printf '  [missing] %-10s %s\n' "$1" "$2"; [ "$3" = req ] && need=1; fi; }
echo "== Leonida-PC doctor =="; echo "OS: $(uname -srm)"; echo "Disk free here: $(df -h . | awk 'NR==2{print $4}')  (Leonida documents ~30 GB staged / ~350 GB full build)"
echo "Required for this repo's tooling:"; chk git "install git" req; chk python3 "install Python 3" req; chk make "install make" req
echo "Needed only for upstream builds (as documented by Leonida; not yet verified by us):"
chk dotnet ".NET 8 SDK" opt; chk cmake "CMake" opt; chk clang "LLVM/clang 21+ with AMDGPU target" opt; chk vulkaninfo "Vulkan SDK/tools" opt
if getent hosts github.com >/dev/null 2>&1; then echo "Network: github.com resolves"; else echo "Network: github.com does NOT resolve (cannot fetch upstream)"; fi
echo "Game files: this project never provides them. Only use a copy you own."
[ "$need" -eq 0 ] && echo "RESULT: ready for 'make check' and 'make fetch-upstream'" || echo "RESULT: install the missing required tools first"
exit "$need"
