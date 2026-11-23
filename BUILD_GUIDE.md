# Build guide
Per upstream: instructions copied verbatim from its README with link + commit SHA. Isolated VM only. Tooling missing in authoring sandbox: cmake, clang, Rust, Go.

## Update 2026-11-23: documented requirements (relayed; not read from upstream by this workspace, nothing built)
- Leonida: Python 3.12+, .NET 8 SDK, Vulkan SDK, LLVM 21+ with AMDGPU target, VS2022 + Windows SDK (Windows runtime). Disk: ~350 GB full build; ~30 GB for selected check/shader/runtime stages. Build staged stages first.
- ProjectReCity: requirements not supplied.
- Xbox2Windows: VS C++ workload, CMake, Ninja, Windows SDK 10.0.26100, Python 3.11+ (full fixture tests).
- AnyPS5: x86-64; CMake 3.22.1+ (3.24+ macOS); Ninja; C++20; GCC/G++ (Linux) / MinGW-w64 GCC (Windows). Source: https://github.com/boykopovar/AnyPS5/blob/main/docs/dev/BUILD.md
Replace with each upstream's verbatim instructions at a pinned SHA once cloned.
