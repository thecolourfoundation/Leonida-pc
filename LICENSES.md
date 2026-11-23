# Licence register
Licences are **reported** (relayed by the user 2026-11-23 from upstream documentation). LICENSE texts, per-file headers, exceptions, third-party notices and vendored licences are **unread**. Not legal advice. Regenerate with `python3 scripts/licence-compat.py` (data: reports/licence-matrix.csv).

## A. Reported licences
| Repo | Licence (reported) | Copyleft | Handling |
|---|---|---|---|
| Leonida | GPL-3.0-or-later | strong | upstream |
| ProjectReCity | GPL-3.0-or-later | strong | derived from Leonida; keep attribution |
| SixNG | GPL-3.0 (-only vs -or-later unknown) | strong | upstream; check headers |
| AnyPS5 | GPL-2.0-only | strong | **isolated** |
| Xbox2Windows | MIT | none | keep separate, preserve notice |
| OpenScarlett | MIT | none | keep separate |
| xbox-emulator | MIT OR Apache-2.0 (dual) | none | check TomBox/rage9 provenance |
| bcpack-rs | MIT OR Apache-2.0 (dual) | none | |
| Percy6Stars | custom non-commercial + attribution + copyleft | restricted | **LINK-ONLY**, see documentation/RESTRICTED_LICENCES.md |
| rpf9-explorer, rpf9, rpf9-extract | UNKNOWN | ? | link-only until read |
| directory, GTAVI-Recomp, PercyStar, GTA6-Asset-Info | UNKNOWN | ? | link-only until read |

## B. Pairwise combination as one combined work (generated)
```
Reported licences (file text NOT yet verified):
  Leonida: GPL-3.0-or-later
  ProjectReCity: GPL-3.0-or-later
  Xbox2Windows: MIT
  AnyPS5: GPL-2.0-only
  OpenScarlett: MIT
  xbox-emulator: MIT OR Apache-2.0
  SixNG: GPL-3.0 (ambiguous: confirm -only vs -or-later)
  bcpack-rs: MIT OR Apache-2.0
  Percy6Stars: CUSTOM-NONCOMMERCIAL
  UNKNOWN (no licence reported): rpf9-explorer, rpf9, rpf9-extract

Matrix (OK / ONEWAY / X / ISO / ?):
              Leonid Projec Xbox2W AnyPS5 OpenSc xbox-e SixNG  bcpack Percy6
Leonida       -      OK     ONEWAY X      ONEWAY ONEWAY OK     ONEWAY ISO   
ProjectReCity OK     -      ONEWAY X      ONEWAY ONEWAY OK     ONEWAY ISO   
Xbox2Windows  ONEWAY ONEWAY -      ONEWAY OK     OK     ONEWAY OK     ISO   
AnyPS5        X      X      ONEWAY -      ONEWAY ONEWAY X      ONEWAY ISO   
OpenScarlett  ONEWAY ONEWAY OK     ONEWAY -      OK     ONEWAY OK     ISO   
xbox-emulator ONEWAY ONEWAY OK     ONEWAY OK     -      ONEWAY OK     ISO   
SixNG         OK     OK     ONEWAY X      ONEWAY ONEWAY -      ONEWAY ISO   
bcpack-rs     ONEWAY ONEWAY OK     ONEWAY OK     OK     ONEWAY -      ISO   
Percy6Stars   ISO    ISO    ISO    ISO    ISO    ISO    ISO    ISO    -     

Problem pairs (X / ISO):
  AnyPS5 + Leonida: X: GPL-2.0-only cannot be combined with GPL-3.x ("or-later" on the other side does not help)
  Leonida + Percy6Stars: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  AnyPS5 + ProjectReCity: X: GPL-2.0-only cannot be combined with GPL-3.x ("or-later" on the other side does not help)
  Percy6Stars + ProjectReCity: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  Percy6Stars + Xbox2Windows: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  AnyPS5 + SixNG: X: GPL-2.0-only cannot be combined with GPL-3.x ("or-later" on the other side does not help)
  AnyPS5 + Percy6Stars: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  OpenScarlett + Percy6Stars: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  Percy6Stars + xbox-emulator: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  Percy6Stars + SixNG: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
  Percy6Stars + bcpack-rs: ISO: restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact
```
Reading it: **X** = GPL-2.0-only (AnyPS5) can never be merged with the GPL-3 projects (Leonida, ReCity, SixNG). **ONEWAY** = permissive code may enter a GPL work, which then follows the GPL (xbox-emulator: choose the MIT option for GPL-2.0-only). **ISO** = Percy6Stars is isolated from everything. Permissive projects remain separately identifiable and keep their notices.

## C. Policy
1. Never merge, link or copy code between AnyPS5 and the GPL-3 projects. Separate repos/builds/artifacts; any interaction only as separate programs, after legal review.
2. Percy6Stars: link-only; never in a commercial distribution without written permission; no code reuse.
3. Workspace commits hold submodule pointers and our own docs/scripts only. No vendored upstream code, no combined distribution. **No code has been copied.**
4. Preserve upstream identities, licence files and notices; ReCity's derivation from Leonida stays documented.
5. "or-later", "GPL-3.0" and dual-licence claims are per-file/per-repo: verify LICENSE text and SPDX headers.
6. A submodule embedded by an upstream (ReCity -> rpf9-explorer) carries its own licence at its pinned commit.
7. Choose a licence for workspace-authored files (open decision).

## D. Documented dependencies and licences
Licences below are **general knowledge, not read from the repos: UNVERIFIED**; these are tools the workspace does not redistribute. Crates, NuGet/pip packages and vendored libraries inside each repo are **unknown** until `scripts/list-vendored.sh` and `scripts/submodule-provenance.sh` run (see documentation/PROVENANCE.md).
| Dependency | Needed by (documented) | Typical licence (unverified) |
|---|---|---|
| Python 3.12+ / 3.11+ | Leonida / Xbox2Windows tests | PSF-2.0 |
| .NET 8 SDK | Leonida | MIT (+ third-party notices) |
| Vulkan SDK | Leonida | LunarG bundle; mostly permissive components (e.g. Apache-2.0); check notices |
| LLVM 21+ (AMDGPU) | Leonida | Apache-2.0 with LLVM exception |
| Visual Studio 2022 / Windows SDK | Leonida runtime; Xbox2Windows | Proprietary Microsoft terms; not redistributable |
| CMake / Ninja | Xbox2Windows; AnyPS5 | BSD-3-Clause / Apache-2.0 |
| GCC/G++ ; MinGW-w64 | AnyPS5 | GPL-3.0-or-later + runtime exception; MinGW-w64 mixed, runtime largely permissive |
| Wine / Proton | Leonida runtime on Linux | Wine LGPL-2.1-or-later; Proton mixed |
| Rust toolchain/crates | xbox-emulator, bcpack-rs, rpf9 (language per user; bcpack-rs unconfirmed) | Rust: MIT OR Apache-2.0; crate licences unknown |
| TomBox, "rage9" | xbox-emulator ("based on") | UNKNOWN |

## E. Open licence concerns
- All LICENSE files unread; AnyPS5's licence source unspecified; SixNG's GPL-3.0 variant unspecified.
- xbox-emulator and ReCity embed or derive from other projects whose licences are unknown.
- Percy6Stars exact terms unread.
- Non-licence legal exposure outranks licence fit: Xbox2Windows, AnyPS5, OpenScarlett, xbox-emulator target console software; confirm no console keys, exploits, dumps or DRM circumvention. Asset tools (SixNG, rpf9*, bcpack-rs): confirm no game-derived data or keys, and that tests use synthetic data. "Clean-room" (rpf9-extract) is a claim to verify.
- No LICENSE file = all rights reserved = link-only.
