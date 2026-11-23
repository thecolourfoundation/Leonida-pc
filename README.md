# GTA VI Cross-Platform Recompilation Research Workspace
Assembles existing public projects as **unmodified upstream submodules**. No new engine code. Nothing here claims GTA VI runs anywhere.
- Status: skeleton only. All upstream data is **UNVERIFIED**; nothing cloned yet (authoring sandbox could not resolve github.com).
- Workflow: ./scripts/add-upstreams.sh <name> -> record-commits.sh -> static-scan.sh -> fill SECURITY_REVIEW.md -> only then build (isolated VM).
- Rules: no game files, assets or keys; no DRM/anti-cheat circumvention; upstream stays pristine (changes go in integrations/ as documented patches).


## Status update 2026-11-23
Five repos are reported remotely verified by the user's research team (second-hand): Leonida, ProjectReCity (derived from Leonida), Xbox2Windows, boykopovar/AnyPS5, awesome-gta6-reverse-engineering. **None cloned, built or tested locally.** See reports/VERIFICATION_STATUS.md, documentation/RELATIONSHIPS.md, documentation/CLONE_SEQUENCE.md.

## Update 2026-11-23
Licences, platform claims and requirements for Leonida, ProjectReCity, Xbox2Windows and AnyPS5 are recorded as remotely inspected documentation (second-hand; nothing cloned/built/tested here). Neither Leonida nor ReCity boots the game. Start with VERIFICATION_CHECKLIST.md, LICENSES.md, COMPATIBILITY.md, INVENTORY.md.
