# Compatibility matrix
**Documented support only. Nothing has been built or tested here.** "Documented" = an upstream page says so (relayed 2026-11-23); it is not evidence the thing works. Values: DOCUMENTED / NOT DOCUMENTED / NOT STATED / UNTESTED. GPU vendor support is NOT STATED anywhere in the supplied information: do not infer it (Leonida's "LLVM with AMDGPU target" is a toolchain requirement, not a vendor-support claim).

| Component | Windows | Linux | macOS | CPU arch | AMD / NVIDIA / Intel | Boots / end-to-end |
|---|---|---|---|---|---|---|
| Leonida: tools + Windows runtime | DOCUMENTED (runtime builds need VS2022 + Windows SDK) | Tools natively DOCUMENTED; Windows runtime via Wine/Proton DOCUMENTED | Apple Silicon: Python + Vulkan test tools DOCUMENTED; runtime via "compatibility arrangements" (unspecified) | x86-64 NOT STATED; ARM64 only for macOS test tools | NOT STATED | **No: game does not boot** |
| Leonida: translator, asset tools, GPU tests | tools DOCUMENTED | DOCUMENTED natively | test tools only (Apple Silicon) | as above | NOT STATED | n/a |
| ProjectReCity | DOCUMENTED target (with Vulkan) | NOT DOCUMENTED | NOT DOCUMENTED | NOT STATED | NOT STATED (GPU research reported) | **No: game does not boot**; Xbox D3D12-to-Vulkan incomplete |
| Xbox2Windows | DOCUMENTED target (x64) | NOT DOCUMENTED | NOT DOCUMENTED | x64 DOCUMENTED; ARM64 NOT DOCUMENTED | NOT STATED | Source-built fixtures + selected shader experiments; full GTA VI startup **unverified** |
| AnyPS5 relinker (PS5 research; not GTA VI) | DOCUMENTED (MinGW-w64 GCC) | DOCUMENTED (GCC/G++) | DOCUMENTED, relinker-only build incl. Apple Silicon | x86-64 required; native-ARM64 vs Rosetta on Apple Silicon **ambiguous: verify** | NOT STATED | N/A |

Rules: Leonida and ReCity are one lineage (not mutual corroboration). AnyPS5 does not contribute to Xbox/GTA VI rows. 350 GB (full Leonida build) / ~30 GB (selected stages) disk is documented; see BUILD_GUIDE.md. Directory-listed repos: no compatibility data.
