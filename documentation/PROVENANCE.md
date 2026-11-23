# Third-party dependency and submodule provenance
Relationships reported 2026-11-23 (second-hand); **no pinned SHA, URL or licence verified for any child**.

| Parent | Relationship (reported) | Child | Open provenance questions |
|---|---|---|---|
| ProjectReCity | derived from | Leonida | fork parent, divergence point, preserved notices |
| ProjectReCity | uses as submodule | breadbbbb/rpf9-explorer | pinned commit, independent licence, owner/history; the GPL-3.0-or-later ReCity tree embeds a repo under its own terms |
| xbox-emulator | "based on" | TomBox | URL, owner, licence; derivation vs dependency vs inspiration |
| xbox-emulator | "based on" | "rage9" (as written) | URL, licence; name differs from the "rpf9" repos: do not conflate until checked |
| SixNG | research relationship only | bcpack-rs | whether it is a dependency at all |
| Leonida and all others | submodules/vendored deps | unknown | enumerate |

Why it matters: xbox-emulator is reported MIT OR Apache-2.0 yet "based on" other projects; if those carry other terms, the stated licence needs checking. Same for ReCity's submodule.

## Procedure (offline-safe, after the hardened clone)
1. `scripts/submodule-provenance.sh upstream/<name>`: lists gitlinks (pinned commits) and `.gitmodules` URLs from the tree without initialising submodules; flags non-github.com hosts. Tested only on a synthetic local repo.
2. `scripts/list-vendored.sh upstream/<name>`: vendored dirs, manifests (incl. Cargo.lock), CMake fetches, nested licence files.
3. Check each child's licence **at the pinned commit**, not the default branch. Add confirmed edges and SHAs here.
4. Ecosystem packages (crates.io, NuGet, pip) arrive at build time: use lockfiles, review before building, build only in the isolated VM.
Record results in reports/ and update LICENSES.md section D.
