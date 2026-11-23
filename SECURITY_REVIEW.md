# Security & legal review
Per-repo checklist (run static-scan.sh first, read hooks manually, VM only):
- [ ] provenance (owner age, history, forks)  - [ ] install/build scripts read  - [ ] binaries/archives  - [ ] secrets  - [ ] network calls  - [ ] supply chain
- [ ] contains/requires game files, dumps or keys?  - [ ] requires DRM/anti-cheat/console-exploit circumvention? -> REJECT
Decision per repo: APPROVE / LINK-ONLY / REJECT + reason. Xbox/PS5-targeting repos get extra scrutiny for exploit/key dependencies.
No repos reviewed yet.


## Update 2026-11-23
No repo has been reviewed. Extra gate for **Xbox2Windows** and **AnyPS5**: confirm they do not require console keys, exploits, dumped firmware/binaries or DRM circumvention before any clone checkout or build. Use the hardened clone procedure in documentation/CLONE_SEQUENCE.md.
