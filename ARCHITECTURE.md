# Architecture map
Areas (capability -> upstream -> evidence): 1 CPU loading/recompilation; 2 shader translation; 3 Vulkan/DX; 4 console syslib compat; 5 memory/address mapping; 6 asset extraction; 7 RPF9/formats; 8 audio/video; 9 input; 10 save/fs; 11 OS abstraction; 12 build/test.
Empty: requires reading upstream code. Dependency map goes in documentation/deps.md.


## Update 2026-11-23
Lineages are tracked separately: (A) Leonida→ReCity, (B) Xbox2Windows, (C) AnyPS5 (PS5 portability research), (D) asset tools. See documentation/RELATIONSHIPS.md. Reported capability evidence so far: Xbox2Windows has documented CPU and shader experiments (reported, not reproduced). Nothing is mapped to the 12 areas yet; code has not been read.

## Update 2026-11-23: documented components (relayed; code not read)
Leonida: translator, asset tools, GPU/Vulkan tests, Windows runtime. ReCity: reports shader, asset, runtime and GPU research; Xbox D3D12-to-Vulkan incomplete. Xbox2Windows: source-built executable fixtures, selected shader experiments. AnyPS5: PS5 relinker (separate track). Mapping to the 12 capability areas is pending code reading; no component is a verified implementation.

## Update 2026-11-23 (relay 3)
Added Xbox translation-layer candidates (OpenScarlett, xbox-emulator), RPF9/BCPack asset tooling (SixNG, rpf9, rpf9-extract, rpf9-explorer, bcpack-rs) and a restricted project (Percy6Stars). See documentation/XBOX_TRANSLATION_COMPARISON.md and BCPACK_TEXTURE_RESEARCH.md. Mapping to the 12 capability areas still awaits code reading.
