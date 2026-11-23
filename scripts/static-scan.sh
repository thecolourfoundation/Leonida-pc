#!/usr/bin/env bash
# Passive static scan only. Never executes anything from upstream.
# Usage: static-scan.sh upstream/<name>  -> reports/scan-<name>.txt
set -uo pipefail; t=${1:?path}; n=$(basename "$t"); out=reports/scan-$n.txt; : > "$out"
{
echo "## binaries / archives / keys by extension"
find "$t" -not -path '*/.git/*' -type f \( -iname '*.exe' -o -iname '*.dll' -o -iname '*.so' -o -iname '*.dylib' -o -iname '*.bin' -o -iname '*.xvd' -o -iname '*.pkg' -o -iname '*.rpf' -o -iname '*.zip' -o -iname '*.7z' -o -iname '*.key' -o -iname '*.pem' -o -iname '*.keys' \)
echo "## ELF/PE magic in files without binary extension"
find "$t" -not -path '*/.git/*' -type f -size +1k | while read -r f; do h=$(head -c4 "$f" | od -An -tx1 | tr -d ' \n'); case $h in 7f454c46|4d5a*) echo "$f";; esac; done
echo "## secret-looking strings"
grep -RInE --exclude-dir=.git '(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' "$t" || true
echo "## install/build hooks (read manually)"
find "$t" -not -path '*/.git/*' \( -name 'setup.py' -o -name 'package.json' -o -name 'Makefile' -o -name 'CMakeLists.txt' -o -name '*.sh' -o -name '*.ps1' -o -name '*.bat' -o -name 'build.rs' -o -name 'Cargo.toml' \)
echo "## network / exec calls in scripts"
grep -RInE --exclude-dir=.git '(curl |wget |Invoke-WebRequest|iex |eval\(|base64 -d|powershell -enc|postinstall|preinstall)' "$t" || true
echo "## DRM/keys/console-exploit keywords (legal triage)"
grep -RIniE --exclude-dir=.git '(prod\.keys|title\.keys|bypass|crack|denuvo|drm|anti-?cheat|jailbreak|kernel exploit)' "$t" | head -200 || true
} >> "$out" 2>&1; echo "wrote $out"
