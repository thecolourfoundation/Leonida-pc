# Verification status (updated 2026-11-23)

**Provenance.** All facts reached this workspace second-hand, in three relays on 2026-11-23: (1) research team verified five repo pages; (2) the user's reading of upstream docs for licences/platforms/requirements; (3) the user's newer upstream documentation for eight further projects and updated README findings. Neither source's own check date was supplied. The author (Claude) has no network access (github.com does not resolve; re-confirmed this session) and verified **none** of it first-hand. No exact commit SHA is known for anything.

## Remotely documented (second-hand)
Core four, licences, platforms and requirements: see INVENTORY.md section A (sources: https://github.com/ItsNotRexed/Leonida, https://github.com/pixl27/ProjectReCity, https://github.com/R0Y00/Xbox2Windows, https://github.com/boykopovar/AnyPS5/blob/main/docs/dev/BUILD.md).

New in relay 3:
- ReCity README: documents AMD, NVIDIA, Intel Vulkan GPU compatibility; AMD native wave64, NVIDIA/Intel wave64 emulation. Documented, not tested by us.
- Xbox2Windows: documents specific GPU hardware testing, CPU recompilation experiments, shader reference comparisons. Full GTA VI startup unverified.
- OpenScarlett (MIT, C++20, Xbox Series compat/translation layer): https://github.com/californiaAlmonds/OpenScarlett
- xbox-emulator (MIT OR Apache-2.0, Rust, based on TomBox and rage9): https://github.com/omonkeyz/xbox-emulator
- SixNG (GPL-3.0, RPF9 extraction CLI+GUI, documents BCPack decoding limitations): https://github.com/holdmysocks/SixNG
- Percy6Stars (non-commercial attribution + copyleft, keep isolated): https://github.com/Ahmet-Dedeler/Percy6Stars
- rpf9-explorer (submodule of ReCity; licence/provenance unknown): https://github.com/breadbbbb/rpf9-explorer
- bcpack-rs (MIT OR Apache-2.0): https://github.com/Ahmet-Dedeler/bcpack-rs
- rpf9-extract (described as clean-room extraction): https://github.com/offs/rpf9-extract
- rpf9 (described as Rust RPF9 library): https://github.com/zeozeozeo/rpf9
Not supplied for these: SHAs, LICENSE text, third-party notices, platforms, requirements, build status, SixNG's actual BCPack limitations, Percy6Stars' purpose and exact terms.

## Unverified locally (everything)
No clone, build, scan or test run; no LICENSE or third-party notice read; no SHA/date/release/owner recorded; no submodule or dependency list read from any repo; no platform or GPU claim reproduced; no code copied. The three new helper scripts were tested only against empty/synthetic inputs. No claim that GTA VI boots, runs or is playable (Leonida and ReCity say it does not boot).
