# Verification status (updated 2026-11-23)

**Provenance.** All facts below reached this workspace second-hand: (1) first relay: the user's research team verified five repo pages; (2) second relay: the user's own reading of upstream GitHub documentation. Both relayed 2026-11-23; neither source's own check date was supplied. The author (Claude) has no network access (github.com does not resolve; confirmed) and has verified **none** of it first-hand. No exact commit SHA is known for anything.

## Remotely documented (second-hand)
| Repo | Licence | Platforms | Requirements | Status | Source |
|---|---|---|---|---|---|
| Leonida | GPL-3.0-or-later | Win tools+runtime; Linux translator/asset tools/GPU tests native + Wine/Proton runtime; macOS Apple Silicon Python+Vulkan test tools | Python 3.12+, .NET 8 SDK, Vulkan SDK, LLVM 21+ w/ AMDGPU, VS2022 + Windows SDK, ~350 GB full / ~30 GB staged | Game does not boot | https://github.com/ItsNotRexed/Leonida |
| ProjectReCity | GPL-3.0-or-later | Windows + Vulkan | not supplied | Game does not boot; shader/asset/runtime/GPU research; Xbox D3D12-to-Vulkan incomplete; derived from Leonida | https://github.com/pixl27/ProjectReCity |
| Xbox2Windows | MIT | x64 Windows | VS C++ workload, CMake, Ninja, Windows SDK 10.0.26100, Python 3.11+ | Fixtures + selected shader experiments; full GTA VI startup unverified | https://github.com/R0Y00/Xbox2Windows |
| AnyPS5 | GPL-2.0-only (licence source not specified) | Linux/Windows relinker; macOS relinker-only incl. Apple Silicon | x86-64, CMake 3.22.1+ (3.24+ macOS), Ninja, C++20, GCC/G++ or MinGW-w64 | not supplied | https://github.com/boykopovar/AnyPS5/blob/main/docs/dev/BUILD.md |
| awesome-gta6-reverse-engineering | n/a | n/a | n/a | curated list | https://github.com/Ahmet-Dedeler/awesome-gta6-reverse-engineering |

Directory-listed names (per user; I could not open the page; claims unverified): omonkeyz/xbox-emulator, californiaAlmonds/OpenScarlett, Freminet/ScarlettX, breadbbbb/rpf9-explorer, holdmysocks/SixNG, Ahmet-Dedeler/Percy6Stars, zeozeozeo/rpf9, Ahmet-Dedeler/bcpack-rs.

## Unverified locally (everything)
No clone, build, scan or test was run. No LICENSE text read, no SHA/date/release/owner recorded, no dependency list read from the repos themselves (the lists above are what the user reported), no platform claim reproduced, no statement about any directory-listed repo. No claim that GTA VI boots, runs or is playable (upstreams themselves say it does not boot).
