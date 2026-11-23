# GPU compatibility evidence
Evidence grades: **E0** nothing stated; **E1** documentation claim; **E2** documentation naming hardware/driver with logs or results we have read; **E3** reproduced by us. **No E3 exists. Nothing here says a GPU works.** All is relayed 2026-11-23.

| Project | AMD | NVIDIA | Intel | Grade | Detail |
|---|---|---|---|---|---|
| ProjectReCity | documented; native wave64 | documented; wave64 emulation | documented; wave64 emulation | E1 | README discusses AMD/NVIDIA/Intel Vulkan compatibility; hardware/driver specifics not supplied; game does not boot |
| Xbox2Windows | not supplied | not supplied | not supplied | E1 (upgrade to E2 after reading hardware list/logs) | documents specific GPU hardware testing, CPU recompilation experiments, shader reference comparisons; full GTA VI startup unverified |
| Leonida | not stated | not stated | not stated | E0 (vendor) | GPU tests exist (native Linux; Apple Silicon Vulkan test tools); AMDGPU is a toolchain requirement, not a vendor claim; game does not boot |
| OpenScarlett, xbox-emulator | not supplied | not supplied | not supplied | E0 | |
| AnyPS5 | n/a | n/a | n/a | E0 | PS5 relinker research, no GPU claims supplied |

## To verify
- Read the ReCity and Xbox2Windows READMEs/logs: exact GPUs, driver versions, Vulkan version/extensions, what was run (shader tests vs anything else).
- General knowledge, unverified: wave64 emulation on hardware with other native subgroup sizes can affect correctness and performance; check how it is implemented and validated.
- Reproduce on available hardware only after builds are approved; record per-vendor results separately.
