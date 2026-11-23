# BCPack and texture-decoding research
Reported facts only (relayed 2026-11-23); nothing inspected or run here.

## Reported
- **SixNG** (GPL-3.0): cross-platform RPF9 asset extraction, CLI and GUI. Its docs explicitly list BCPack decoding limitations (the limitations themselves were not supplied).
- **bcpack-rs** (MIT OR Apache-2.0): to be researched for its implementation and compatibility with SixNG. Language not stated ("-rs" suggests Rust: unverified).
- **rpf9** (zeozeozeo): described as a Rust RPF9 library. **rpf9-extract** (offs): described as a clean-room extraction approach (claim to verify). **rpf9-explorer** (breadbbbb): used as a submodule by ReCity; licence/provenance unknown.
- General knowledge, unverified: BCPack is a Microsoft texture-compression scheme layered over BCn formats on Xbox Series.

## Landscape
| Tool | Form | Licence (reported) | Notes |
|---|---|---|---|
| SixNG | CLI + GUI | GPL-3.0 | documents BCPack limits |
| bcpack-rs | library/impl (TO INSPECT) | MIT OR Apache-2.0 | candidate BCPack implementation |
| rpf9 | Rust library | UNKNOWN | RPF9 container parsing |
| rpf9-extract | extractor | UNKNOWN | "clean-room" claim |
| rpf9-explorer | explorer (TO INSPECT) | UNKNOWN | ReCity submodule |
| Leonida asset tools | tools | GPL-3.0-or-later | part of Leonida |

## Open questions
1. What does bcpack-rs implement (decode, encode, or both) and with what coverage?
2. Does SixNG use bcpack-rs, its own decoder, or neither? Which BCPack cases does SixNG say it cannot decode?
3. Licence fit: permissive bcpack-rs into GPL-3.0 SixNG is one-way compatible (check Apache-2.0 vs MIT option and notices) if code is ever embedded. No code is copied now.
4. Language/API boundary between SixNG and bcpack-rs (library, FFI, subprocess).
5. Provenance of BCPack knowledge: clean-room vs reverse-engineered; any dependency on proprietary SDK material.
6. Test data: tests must use synthetic vectors; reject anything shipping game-derived textures/archives. We hold no game files, so only static analysis is possible.
7. Output path: decoded BCn to Vulkan upload; which tools overlap with Leonida/ReCity asset work.
