# Licence register
| Repo | Licence (from LICENSE file) | Third-party | Copyleft? | Submodule OK? | Notes |
|---|---|---|---|---|---|
All rows UNVERIFIED. No licence file = all rights reserved: link only, do not copy. Never merge incompatible licences into one distributed artifact.


## Compatibility concerns identified so far (2026-11-23)
No licence texts have been read by this workspace; the research team supplied none. These are structural concerns, not conclusions.
1. **Leonida → ProjectReCity (derivative):** ReCity must comply with Leonida's licence. If Leonida is copyleft (GPL/AGPL/MPL) ReCity's terms are constrained; if Leonida has **no licence**, ReCity's derivation may itself be unlicensed. Check both repos' LICENSE files and ReCity's fork/commit history before treating either as redistributable.
2. **Missing licence = all rights reserved.** Any repo without a LICENSE file: link-only submodule, no copying, no combined distribution.
3. **Copyleft mixing:** if the set includes GPL-family and permissive or incompatible-copyleft code (e.g. GPLv2-only vs GPLv3/Apache-2.0), they must not be linked into one binary/distribution. A submodule reference is not redistribution, but any combined build or release is.
4. **Third-party code inside upstreams** (emulator cores, shader translators, vendored libs, console SDK headers) may carry different licences from the repo's top-level one; scan each upstream's `third_party`/vendored dirs.
5. **Non-licence legal exposure (outranks licence compatibility):** Xbox2Windows and AnyPS5 target console software. If either depends on console keys, exploits, dumped firmware/binaries, or DRM circumvention, it is excluded under project rules regardless of its software licence. Not yet checked.
6. **Game-derived content:** any repo containing GTA VI assets, extracted data, symbols derived from proprietary binaries, or keys must be rejected or link-only. Applies especially to the gta6-assets category.
7. **Awesome-list:** list content licence (often CC0/none) does not cover linked projects.

Register rows below stay UNVERIFIED until a human reads each LICENSE.
