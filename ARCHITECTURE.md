# Architecture map
Areas (capability -> upstream -> evidence): 1 CPU loading/recompilation; 2 shader translation; 3 Vulkan/DX; 4 console syslib compat; 5 memory/address mapping; 6 asset extraction; 7 RPF9/formats; 8 audio/video; 9 input; 10 save/fs; 11 OS abstraction; 12 build/test.
Empty: requires reading upstream code. Dependency map goes in documentation/deps.md.


## Update 2026-11-23
Lineages are tracked separately: (A) Leonida→ReCity, (B) Xbox2Windows, (C) AnyPS5 (PS5 portability research), (D) asset tools. See documentation/RELATIONSHIPS.md. Reported capability evidence so far: Xbox2Windows has documented CPU and shader experiments (reported, not reproduced). Nothing is mapped to the 12 areas yet; code has not been read.
