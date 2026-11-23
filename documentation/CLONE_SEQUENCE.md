# Prioritized clone & build sequence (for when connectivity returns)
Nothing below has been executed. Use only the canonical github.com URLs in scripts/repos.txt: no mirrors, no zip/binary downloads, no installers. Work in a throwaway VM with no secrets and no game files.

## Hardened clone procedure (per repo)
1. `git clone --no-checkout --no-recurse-submodules -c core.hooksPath=/dev/null -c protocol.file.allow=never <url> upstream/<name>`  (also `GIT_LFS_SKIP_SMUDGE=1`)
2. Record identity first: `git -C upstream/<name> log -1 --format='%H %cI'`, `git tag`, owner/fork parent from the GitHub page.
3. Inspect before checkout: `git ls-tree -r --name-only HEAD`, read `.gitmodules`, LICENSE, README, CI files, build scripts via `git show HEAD:<file>`.
4. Only then `git checkout`, run `scripts/static-scan.sh`, fill SECURITY_REVIEW.md.
5. Decide APPROVE / LINK-ONLY / REJECT. Only approved repos get `git submodule add` and any build.

## Order
| # | Repo | Why this position | Gate before build |
|---|---|---|---|
| 1 | awesome-gta6-reverse-engineering | Docs-only, lowest risk. Enumerates further leads. | Triage each linked repo; verify remotely before cloning. |
| 2 | Leonida | Root of one lineage; needed to evaluate ReCity. | Licence read; keys/assets/DRM check; scripts read. |
| 3 | ProjectReCity | Derived from Leonida; diff against it to isolate additions. | As #2 plus licence-inheritance check. |
| 4 | Xbox2Windows | Only reported CPU + shader experiments; highest technical value. | Console key/exploit/dump dependency check first; claims vs. reproducible evidence. |
| 5 | AnyPS5 | Separate PS5 track; clone for analysis in its own category. | Same console-exploit/key legal gate; keep out of Xbox matrix. |
| 6 | gta6-assets (rpf9, rpf9-extract, GTA6-Asset-Info) | Not before team verification. | Must not need or ship game archives/keys. Read-only analysis. |
| 7 | xbox-emu, other gta6-re/recomp repos | Not before team verification. | Per-repo verification, then steps above. |

## Build/test order (after approval)
Build each approved repo independently, in order 2, 4, 5, then others. Use `scripts/record-build.sh <repo> -- <cmd>`. Run upstream tests before any integration. Do not combine projects until each one's standalone behaviour is recorded. Tooling still to install in the build VM: cmake, clang (and Rust/Go/etc. as each README requires).
