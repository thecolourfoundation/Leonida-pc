#!/usr/bin/env bash
# Passive: lists submodules, vendored dirs, dependency manifests and nested licence files per upstream. Runs nothing from upstream.
# Usage: list-vendored.sh [upstream/<name> ...]   -> reports/vendored-<name>.txt
set -uo pipefail; cd "$(dirname "$0")/.."
targets=("$@"); [ ${#targets[@]} -gt 0 ] || targets=(upstream/*/)
for t in "${targets[@]}"; do [ -d "$t" ] || continue; n=$(basename "$t"); out=reports/vendored-$n.txt
{ echo "## .gitmodules"; cat "$t/.gitmodules" 2>/dev/null || echo "(none)"
  echo "## vendored-looking dirs"; find "$t" -not -path '*/.git/*' -type d \( -iname third_party -o -iname thirdparty -o -iname vendor -o -iname extern -o -iname external -o -iname deps \)
  echo "## dependency manifests"; find "$t" -not -path '*/.git/*' -type f \( -name requirements*.txt -o -name pyproject.toml -o -name '*.csproj' -o -name packages.config -o -name vcpkg.json -o -name 'conanfile*' -o -name Cargo.toml -o -name Cargo.lock -o -name package.json -o -name CMakeLists.txt -o -name '*.cmake' \)
  echo "## CMake fetches (FetchContent/ExternalProject/find_package)"; grep -RInE --exclude-dir=.git '(FetchContent_Declare|ExternalProject_Add|find_package\()' "$t" 2>/dev/null | head -100
  echo "## licence files at any depth"; find "$t" -not -path '*/.git/*' -type f -iregex '.*/\(licen[sc]e\|copying\|notice\)[^/]*'
} > "$out" 2>&1; echo "wrote $out"; done
