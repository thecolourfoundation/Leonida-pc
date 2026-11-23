# Licence register
Licences below are **reported** (relayed by the user 2026-11-23 from upstream GitHub documentation). LICENSE file text, per-file SPDX headers, exceptions and vendored third-party licences have **not** been read here. Not legal advice. Triage tool: `python3 scripts/licence-compat.py`.

## A. Matrix (reported)
| Repo | SPDX (reported) | Copyleft | Role in workspace |
|---|---|---|---|
| Leonida | GPL-3.0-or-later | strong | upstream submodule |
| ProjectReCity | GPL-3.0-or-later | strong | upstream submodule; derived from Leonida; keep attribution |
| Xbox2Windows | MIT | none | upstream submodule; keep separate, preserve MIT notice |
| AnyPS5 | GPL-2.0-only | strong | upstream submodule; **isolated** |
| directory + 8 listed repos + 4 other assignment repos | UNKNOWN | ? | link-only until read |

## B. Pairwise combination (as one combined work)
| Pair | Verdict |
|---|---|
| Leonida + ProjectReCity | OK: same licence; ReCity is a derivative, so Leonida's copyright notices/attribution must stay intact |
| Leonida/ReCity + Xbox2Windows | OK one-way: MIT code can sit inside a GPL-3 work (combined work is GPL-3, MIT notice kept). Still keep separate |
| Leonida/ReCity + AnyPS5 | **INCOMPATIBLE** as one combined work. GPL-2.0-only cannot be combined with GPL-3.x code, and "or-later" on Leonida/ReCity does not fix that |
| Xbox2Windows + AnyPS5 | OK one-way into GPL-2.0-only; keep separate |

## C. Policy
1. Never merge, link or copy code between AnyPS5 and Leonida/ReCity. Separate repos, builds and release artifacts; if they ever interact, only as separate programs (CLI/files), and only after legal review.
2. Workspace commits contain submodule pointers and our own docs/scripts only, never vendored upstream code. Nothing here is a combined distribution.
3. MIT components keep their own LICENSE and notice, preserved separately.
4. ReCity: preserve its relationship to Leonida and all inherited notices; confirm fork parent and history from git.
5. "or-later" is a per-file claim: verify SPDX headers/LICENSE text before relying on it.
6. Choose a licence for workspace-authored files (open decision; see VERIFICATION_CHECKLIST.md).

## D. Documented dependencies and their licences
Licences in this table are **general knowledge, not read from the upstream repos: UNVERIFIED**. These are build/runtime tools the workspace does not redistribute. Libraries vendored or fetched *inside* each repo are **unknown** (run `scripts/list-vendored.sh` after cloning).
| Dependency | Needed by (documented) | Typical licence (unverified) |
|---|---|---|
| Python 3.12+ / 3.11+ | Leonida / Xbox2Windows fixture tests | PSF-2.0 |
| .NET 8 SDK | Leonida | MIT (plus bundled third-party notices) |
| Vulkan SDK | Leonida | LunarG SDK bundle; components under several mostly permissive licences (e.g. Apache-2.0); check SDK notices |
| LLVM 21+ (AMDGPU target) | Leonida | Apache-2.0 with LLVM exception |
| Visual Studio 2022 / Windows SDK (10.0.26100 for Xbox2Windows) | Leonida runtime; Xbox2Windows | Proprietary Microsoft terms; not redistributable |
| CMake | Xbox2Windows; AnyPS5 (3.22.1+, 3.24+ macOS) | BSD-3-Clause |
| Ninja | Xbox2Windows; AnyPS5 | Apache-2.0 |
| GCC/G++ | AnyPS5 (Linux) | GPL-3.0-or-later with GCC Runtime Library Exception |
| MinGW-w64 GCC | AnyPS5 (Windows) | Mixed (runtime largely permissive e.g. ZPL/public domain; compiler as GCC) |
| Wine / Proton | Leonida Windows runtime on Linux | Wine LGPL-2.1-or-later; Proton bundles components under various licences |
| macOS compiler/toolchain | AnyPS5 macOS | Not specified in supplied info |

## E. Open licence concerns
- LICENSE files and headers unread for all repos; AnyPS5's source for its licence claim unspecified.
- Vendored/fetched third-party code in each upstream unknown (may carry other licences).
- Toolchain runtimes (MSVC redistributables, GCC runtime) matter only if we ever ship binaries; we do not.
- Non-licence legal exposure outranks licence compatibility: Xbox2Windows and AnyPS5 target console software; confirm no console keys, exploits, dumped firmware/binaries or DRM circumvention.
- Any repo with game-derived content (assets, symbols from proprietary binaries, keys) is rejected or link-only; especially gta6-assets.
- A repo with no LICENSE file is all-rights-reserved: link only.
