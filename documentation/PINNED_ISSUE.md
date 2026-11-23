# Pinned issue text (copy into a new issue and pin it)
**Title:** Help wanted: first verified facts about upstream Leonida

GTA VI does **not** boot with Leonida today, and this repo has no launcher or game files. This is a verification workspace. Everything is blocked on real upstream facts, which need a networked machine (hardware only for later stages).

Do this (about 5 minutes):
1. `git clone` this repo, then `make doctor`, `make check`, `make fetch-upstream`.
2. Open an **Upstream identity report** issue with `reports/upstream-identity.txt`.

Later, with hardware: build one staged stage in an isolated VM via `scripts/record-build.sh` and file a **Build / test stage result**. Order: asset tools, shader translation, SPIR-V validation, runtime, D3D12-to-Vulkan layer. Legal lines: no leaked or proprietary game data, no keys, no DRM or console-security bypass. Beware fake "GTA VI PC" installers (malware).
Other help: map Leonida's components from its source; add regression tests; pin the CI actions to commit SHAs.
