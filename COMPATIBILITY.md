# Compatibility matrix
**Documented support only. Nothing has been built or tested here.** DOCUMENTED = an upstream page says so (relayed 2026-11-23), not evidence it works. GPU grades E0-E3 are defined in documentation/GPU_COMPATIBILITY_EVIDENCE.md; no E3 exists.

| Component | Windows | Linux | macOS | CPU arch | AMD / NVIDIA / Intel | Boots / end-to-end |
|---|---|---|---|---|---|---|
| Leonida (tools + Windows runtime) | DOCUMENTED (runtime builds need VS2022 + Windows SDK) | tools native; Windows runtime via Wine/Proton | Apple Silicon: Python + Vulkan test tools; runtime via unspecified "compatibility arrangements" | x86-64 NOT STATED; ARM64 only macOS test tools | NOT STATED (E0) | No (documented) |
| Leonida (translator, asset tools, GPU tests) | tools | native | test tools only | as above | NOT STATED | n/a |
| ProjectReCity | DOCUMENTED target (+ Vulkan) | NOT DOCUMENTED | NOT DOCUMENTED | NOT STATED | DOCUMENTED, E1: AMD native wave64; NVIDIA + Intel wave64 emulation | No; Xbox D3D12-to-Vulkan incomplete |
| Xbox2Windows | DOCUMENTED target (x64) | NOT DOCUMENTED | NOT DOCUMENTED | x64 documented; ARM64 not | specific GPU hardware testing documented, E1 (hardware list not supplied) | Fixtures + CPU recompilation experiments + shader reference comparisons; full GTA VI startup unverified |
| OpenScarlett (C++20, MIT) | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED |
| xbox-emulator (Rust, MIT OR Apache-2.0) | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED |
| SixNG (RPF9 extraction, CLI + GUI) | "cross-platform" claim; OS list NOT SUPPLIED | same | same | NOT SUPPLIED | n/a | BCPack decoding limitations documented upstream |
| bcpack-rs / rpf9 / rpf9-explorer / rpf9-extract | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | NOT SUPPLIED | n/a | n/a |
| Percy6Stars | NOT SUPPLIED (link-only) | | | | | |
| AnyPS5 relinker (PS5 research; not GTA VI) | DOCUMENTED (MinGW-w64 GCC) | DOCUMENTED (GCC/G++) | DOCUMENTED, relinker-only incl. Apple Silicon | x86-64 required; Apple Silicon native vs Rosetta unclear | n/a (E0) | N/A |

Rules: Leonida and ReCity are one lineage. AnyPS5 does not contribute to the Xbox/GTA VI rows. Disk: ~350 GB full Leonida build / ~30 GB staged. Neither Leonida nor ReCity boots the game; nothing here supports a playability claim.
