# Remaining verification checklist (run when connectivity returns; none done yet)
Use only canonical github.com URLs; hardened clone procedure in documentation/CLONE_SEQUENCE.md. Isolated VM, no secrets, no game files.

## 1. Identity
- [ ] Exact HEAD SHA, commit date, tags/releases per repo via git (`scripts/record-commits.sh`); no values are recorded today
- [ ] Owner/maintainers, default branch, activity (commit history) per repo
- [ ] ReCity: confirm fork parent = Leonida, divergence point, what ReCity adds (git history)
## 2. Licences
- [ ] Read actual LICENSE files; confirm GPL-3.0-or-later (Leonida, ReCity), MIT (Xbox2Windows), GPL-2.0-only (AnyPS5); find AnyPS5's authoritative licence source
- [ ] Per-file SPDX/headers: "or-later" really applies; no mixed headers or extra exceptions
- [ ] ReCity keeps Leonida copyright notices/attribution
- [ ] Enumerate vendored/fetched deps + their licences (`scripts/list-vendored.sh`); replace the unverified general-knowledge table in LICENSES.md
- [ ] Re-run `scripts/licence-compat.py` on verified data; legal review before any combined artifact
- [ ] Decide licence for workspace-authored files
## 3. Legal / safety
- [ ] `scripts/static-scan.sh` each approved repo; read build scripts before running anything
- [ ] Xbox2Windows and AnyPS5: no console keys, exploits, dumped firmware/binaries or DRM circumvention
- [ ] No game files, assets, keys or derived proprietary data in any repo (esp. gta6-assets)
## 4. Platform claims (reproduce each; DOCUMENTED is not WORKS)
- [ ] Leonida: Windows tools/runtime; Linux native translator/asset tools/GPU tests; Wine/Proton runtime; macOS Apple Silicon test tools; what "compatibility arrangements" means
- [ ] ReCity: Windows + Vulkan target; Linux/macOS status
- [ ] Xbox2Windows: fixtures build and pass; shader experiments reproducible; any startup evidence
- [ ] AnyPS5: Linux/Windows/macOS relinker builds; Apple Silicon native ARM64 or Rosetta
- [ ] GPU vendors (AMD/NVIDIA/Intel) and CPU arch (x86-64/ARM64): record only what tests show
- [ ] Re-check "game does not boot" at the pinned SHAs
## 5. Build hosts and staging
- [ ] Host with ~350 GB free for full Leonida build; start with ~30 GB staged check/shader/runtime builds
- [ ] Toolchains: Python 3.12+, .NET 8, Vulkan SDK, LLVM 21+ (AMDGPU), VS2022 + Windows SDK, CMake/Ninja, GCC/MinGW-w64, per OS; record versions
- [ ] Build each repo independently; log with `scripts/record-build.sh`; run upstream tests before any integration
## 6. Ecosystem triage (directory claims are not evidence)
- [ ] Verify remotely, then triage: xbox-emulator, OpenScarlett, ScarlettX, rpf9-explorer, SixNG, Percy6Stars, rpf9, bcpack-rs (+ GTAVI-Recomp, PercyStar, rpf9-extract, GTA6-Asset-Info)
- [ ] Walk the rest of the directory's links
