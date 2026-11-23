# Inventory
**Nothing here was cloned, built, scanned or tested locally.** Entries are remotely inspected documentation relayed by the user on 2026-11-23 (reports/VERIFICATION_STATUS.md). Latest commit SHAs/dates/releases/owners are **not recorded**: get them with git later (`scripts/record-commits.sh`). Manifest-driven table: `scripts/gen-inventory.sh`.

## A. Core upstreams
| Repo (URL) | Category | Licence (reported) | Targets (documented) | Documented requirements | Reported status |
|---|---|---|---|---|---|
| Leonida https://github.com/ItsNotRexed/Leonida | gta6-re (lineage root) | GPL-3.0-or-later | Win tools+runtime; Linux translator/asset tools/GPU tests native + Wine/Proton runtime; macOS Apple Silicon Python+Vulkan test tools | Python 3.12+, .NET 8, Vulkan SDK, LLVM 21+ w/ AMDGPU, VS2022 + Windows SDK; ~350 GB full / ~30 GB staged | Game does not boot |
| ProjectReCity https://github.com/pixl27/ProjectReCity | gta6-re (derived from Leonida) | GPL-3.0-or-later | Windows + Vulkan | not supplied | Does not boot; README documents AMD/NVIDIA/Intel Vulkan GPU compatibility (AMD native wave64; NVIDIA/Intel wave64 emulation); Xbox D3D12-to-Vulkan incomplete; uses rpf9-explorer as submodule |
| Xbox2Windows https://github.com/R0Y00/Xbox2Windows | xbox-recomp | MIT | x64 Windows | VS C++ workload, CMake, Ninja, Windows SDK 10.0.26100, Python 3.11+ | Fixtures, CPU recompilation experiments, shader reference comparisons, specific GPU hardware testing documented; full GTA VI startup unverified |
| AnyPS5 https://github.com/boykopovar/AnyPS5 | ps5-portability (separate) | GPL-2.0-only | Linux/Windows relinker; macOS relinker-only incl. Apple Silicon | x86-64, CMake 3.22.1+ (3.24+ macOS), Ninja, C++20, GCC / MinGW-w64 | not supplied |
| awesome-gta6-reverse-engineering https://github.com/Ahmet-Dedeler/awesome-gta6-reverse-engineering | directory | not supplied | n/a | n/a | Curated list; claims are not build results |

## B. Newly documented projects (reported; unverified)
| Repo | Category | Licence (reported) | Reported description | Handling |
|---|---|---|---|---|
| californiaAlmonds/OpenScarlett | xbox-emu | MIT | C++20; Xbox Series compatibility and translation layer | compare vs Leonida/Xbox2Windows |
| omonkeyz/xbox-emulator | xbox-emu | MIT OR Apache-2.0 | Rust; Xbox Series compatibility, based on TomBox and rage9 | check provenance of TomBox/rage9 |
| holdmysocks/SixNG | gta6-assets | GPL-3.0 (-only vs -or-later unspecified) | cross-platform RPF9 extraction, CLI + GUI; documents BCPack decoding limitations | BCPack research |
| Ahmet-Dedeler/bcpack-rs | gta6-assets | MIT OR Apache-2.0 | research implementation and SixNG compatibility | BCPack research |
| Ahmet-Dedeler/Percy6Stars | gta6-re | CUSTOM non-commercial + attribution + copyleft (text unread) | purpose not supplied | **LINK-ONLY, licence-isolated** |
| breadbbbb/rpf9-explorer | gta6-assets | UNKNOWN | submodule of ReCity | inspect licence/provenance |
| zeozeozeo/rpf9 | gta6-assets | UNKNOWN | Rust RPF9 library | inspect |
| offs/rpf9-extract | gta6-assets | UNKNOWN | described as clean-room extraction | inspect claim; status UNVERIFIED |

## C. Still unverified
JamesCicada/GTAVI-Recomp, rpatty-dev/PercyStar, TrinitronClient/GTA6-Asset-Info; the directory's other links.

New analysis docs: documentation/XBOX_TRANSLATION_COMPARISON.md, BCPACK_TEXTURE_RESEARCH.md, GPU_COMPATIBILITY_EVIDENCE.md, RESTRICTED_LICENCES.md, PROVENANCE.md.
