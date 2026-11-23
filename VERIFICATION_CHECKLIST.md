# Remaining verification checklist (run when connectivity returns; none done yet)
Canonical github.com URLs only; hardened clone procedure in documentation/CLONE_SEQUENCE.md. Isolated VM, no secrets, no game files, no code copying.

## 1. Identity
- [ ] Exact HEAD SHA, date, tags/releases per repo via git (`scripts/record-commits.sh`)
- [ ] Owner/maintainers, default branch, activity per repo
- [ ] ReCity: fork parent = Leonida, divergence point, additions
## 2. Licences (inspect each actual LICENSE file and third-party notices)
- [ ] Leonida, ReCity (GPL-3.0-or-later), SixNG (GPL-3.0: -only or -or-later?), AnyPS5 (GPL-2.0-only; find licence source), Xbox2Windows, OpenScarlett (MIT), xbox-emulator, bcpack-rs (MIT OR Apache-2.0)
- [ ] Percy6Stars: read verbatim terms (non-commercial, attribution, copyleft); record in RESTRICTED_LICENCES.md; stays link-only
- [ ] rpf9-explorer, rpf9, rpf9-extract, GTAVI-Recomp, PercyStar, GTA6-Asset-Info: licence unknown, read
- [ ] Per-file SPDX headers ("or-later" really applies); no extra exceptions
- [ ] Re-run `scripts/licence-compat.py` on verified data; legal review before any combined artifact
- [ ] Choose licence for workspace-authored files
## 3. Provenance and dependencies (documentation/PROVENANCE.md)
- [ ] `scripts/submodule-provenance.sh` + `scripts/list-vendored.sh` on each clone
- [ ] ReCity's rpf9-explorer submodule: pinned SHA, URL host, licence at that SHA, owner history
- [ ] xbox-emulator: identify TomBox and "rage9" (URLs, licences, relationship type); confirm the stated licence is justified
- [ ] Rust (Cargo.lock), .NET, Python dependency lists and licences; replace the unverified table in LICENSES.md section D
## 4. Legal / safety
- [ ] `scripts/static-scan.sh` each approved repo; read build scripts first
- [ ] Console-targeting repos (Xbox2Windows, AnyPS5, OpenScarlett, xbox-emulator, Leonida/ReCity): no console keys, exploits, dumped firmware/binaries, DRM circumvention
- [ ] Asset tools (SixNG, rpf9*, bcpack-rs): no game-derived data/keys shipped; tests use synthetic data; verify rpf9-extract "clean-room" claim
## 5. Platform and GPU claims (reproduce; DOCUMENTED is not WORKS)
- [ ] Leonida, ReCity, Xbox2Windows, AnyPS5 claims per COMPATIBILITY.md; AnyPS5 Apple Silicon native vs Rosetta
- [ ] ReCity GPU claims: exact GPUs/drivers/Vulkan versions; wave64 native vs emulation implementation (GPU_COMPATIBILITY_EVIDENCE.md)
- [ ] Xbox2Windows: hardware list/logs behind GPU testing; shader reference comparison method; CPU recompilation experiment scope; any startup evidence
- [ ] OpenScarlett, xbox-emulator: platforms, approach, evidence (XBOX_TRANSLATION_COMPARISON.md)
- [ ] Re-check "game does not boot" at pinned SHAs
## 6. BCPack/texture research (BCPACK_TEXTURE_RESEARCH.md)
- [ ] SixNG's documented BCPack limitations (actual list); does it use bcpack-rs?
- [ ] bcpack-rs scope and API; language boundary with SixNG; provenance of BCPack knowledge
## 7. Build hosts and staging
- [ ] ~350 GB host for full Leonida build; start with ~30 GB staged builds
- [ ] Toolchains per OS (Python, .NET 8, Vulkan SDK, LLVM 21+, VS2022/Windows SDK, CMake/Ninja, GCC/MinGW-w64, Rust); record versions
- [ ] Build each repo independently; log with `scripts/record-build.sh`; upstream tests before integration
## 8. Ecosystem
- [ ] Verify remotely, then triage GTAVI-Recomp, PercyStar, GTA6-Asset-Info; walk the rest of the directory's links
