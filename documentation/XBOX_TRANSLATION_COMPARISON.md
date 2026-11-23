# Xbox translation-layer comparison
Basis: facts relayed by the user 2026-11-23 from upstream documentation; **nothing inspected, built or tested here**. "TO INSPECT" = unknown until the code is read. Directory/README claims are not evidence.

| Project | Licence (reported) | Language / tooling (documented) | Stated purpose | Host target | Evidence reported | GTA VI boots? |
|---|---|---|---|---|---|---|
| Leonida | GPL-3.0-or-later | Python 3.12+, .NET 8, LLVM 21+ (AMDGPU), Vulkan SDK (per-component languages not stated) | translator, asset tools, GPU tests, Windows runtime | Win; Linux native tools + Wine/Proton runtime; macOS Apple Silicon test tools | GPU tests documented | No (documented) |
| ProjectReCity | GPL-3.0-or-later | not supplied | derived from Leonida; shader/asset/runtime/GPU research | Windows + Vulkan | README documents AMD/NVIDIA/Intel Vulkan compatibility (not tested by us) | No; Xbox D3D12-to-Vulkan incomplete |
| Xbox2Windows | MIT | VS C++ workload, CMake, Ninja, Windows SDK 10.0.26100, Python 3.11+ tests | CPU recompilation experiments, executable fixtures, shader reference comparisons | x64 Windows | Specific GPU hardware testing documented (hardware list not supplied) | Full startup unverified |
| OpenScarlett | MIT | C++20 | Xbox Series compatibility and translation layer | not supplied | not supplied | not supplied |
| xbox-emulator | MIT OR Apache-2.0 | Rust | Xbox Series compatibility, based on TomBox and rage9 | not supplied | not supplied | not supplied |

## What to extract from the code (all TO INSPECT)
Approach (static recompilation / dynamic translation / emulation / HLE); executable loading; kernel/system-API layer; memory and address mapping; D3D12-to-Vulkan path; shader translation and reference-comparison method; filesystem/saves/input/audio; tests and CI; whether any claim is reproducible without game files.

## Comparison notes
- General knowledge, unverified: Xbox Series hardware is x86-64 CPU + RDNA 2 GPU, so "CPU recompilation" is mostly an OS/ABI/API-layer problem rather than ISA translation. Confirm what each project actually does.
- OpenScarlett and xbox-emulator are separate Xbox compatibility efforts: compare against Leonida and Xbox2Windows for duplicated vs complementary work. Overlap unknown.
- xbox-emulator is "based on" TomBox and rage9: see PROVENANCE.md (relationship type and licences unknown).
- Leonida and ReCity are one lineage; they do not corroborate each other.
- Licence view (see LICENSES.md): OpenScarlett/xbox-emulator are permissive and one-way compatible with the GPL projects; no code is to be copied yet.
