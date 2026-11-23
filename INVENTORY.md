# Inventory
**Nothing here was cloned, built, scanned or tested locally.** Entries are remotely inspected documentation, relayed by the user on 2026-11-23 (see reports/VERIFICATION_STATUS.md). Latest commit SHAs, dates, releases and owners/maintainers are **not recorded**: retrieve with git when connectivity returns (reports/upstream-commits.tsv via scripts/record-commits.sh). Regenerate the manifest-driven table with `scripts/gen-inventory.sh`.

## A. Core upstreams (remote docs inspected)
| Repo (URL) | Category | Licence (reported) | Targets / platforms (documented) | Documented requirements | Reported status |
|---|---|---|---|---|---|
| Leonida https://github.com/ItsNotRexed/Leonida | gta6-re (root of lineage) | GPL-3.0-or-later | Windows: tools + runtime. Linux: translator, asset tools, GPU tests natively; Windows runtime via Wine/Proton. macOS Apple Silicon: Python + Vulkan test tools; Windows runtime via compatibility arrangements | Python 3.12+; .NET 8 SDK; Vulkan SDK; LLVM 21+ with AMDGPU target; Visual Studio 2022 + Windows SDK (Windows runtime builds); ~350 GB free for full build, ~30 GB for selected check/shader/runtime stages | **Game does not boot** |
| ProjectReCity https://github.com/pixl27/ProjectReCity | gta6-re (derived from Leonida) | GPL-3.0-or-later | Windows with Vulkan | Not supplied | **Game does not boot.** README reports shader, asset, runtime and GPU research; Xbox D3D12-to-Vulkan incomplete |
| Xbox2Windows https://github.com/R0Y00/Xbox2Windows | xbox-recomp | MIT | x64 Windows | Visual Studio C++ workload; CMake; Ninja; Windows SDK 10.0.26100; Python 3.11+ (full fixture tests) | Source-built executable fixtures and selected shader experiments; **full GTA VI startup unverified** |
| AnyPS5 https://github.com/boykopovar/AnyPS5 (docs: .../blob/main/docs/dev/BUILD.md) | ps5-portability (separate; not an Xbox GTA VI implementation) | GPL-2.0-only | Linux and Windows relinker; macOS relinker-only build incl. Apple Silicon | x86-64; CMake 3.22.1+ (3.24+ on macOS); Ninja; C++20; GCC/G++ (Linux); MinGW-w64 GCC (Windows) | Not supplied |
| awesome-gta6-reverse-engineering https://github.com/Ahmet-Dedeler/awesome-gta6-reverse-engineering | directory | Not supplied (list licence does not cover linked projects) | n/a | n/a | Curated list; claims are not build results |

Canonical AnyPS5 = boykopovar/AnyPS5 only. Leonida and ReCity are one lineage, not independent implementations.

## B. Ecosystem listed in the directory (per user; **not independently verified; I could not open the directory page myself**)
| Repo | Category | Status |
|---|---|---|
| omonkeyz/xbox-emulator | xbox-emu | DIRECTORY-LISTED |
| californiaAlmonds/OpenScarlett | xbox-emu | DIRECTORY-LISTED |
| Freminet/ScarlettX | xbox-emu | DIRECTORY-LISTED |
| holdmysocks/SixNG | gta6-re | DIRECTORY-LISTED |
| Ahmet-Dedeler/Percy6Stars | gta6-re | DIRECTORY-LISTED |
| zeozeozeo/rpf9 | gta6-assets | DIRECTORY-LISTED |
| breadbbbb/rpf9-explorer | gta6-assets | DIRECTORY-LISTED (new) |
| Ahmet-Dedeler/bcpack-rs | gta6-assets (category tentative, from the name only) | DIRECTORY-LISTED (new) |
Purpose, licence, platforms, activity and legality are all unknown for these. On the original assignment list but not named in the latest directory excerpt (so still UNVERIFIED, not "absent"): JamesCicada/GTAVI-Recomp, rpatty-dev/PercyStar, offs/rpf9-extract, TrinitronClient/GTA6-Asset-Info. The directory's other linked repos are untriaged.
