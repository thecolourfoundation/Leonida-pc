# GTA VI Cross-Platform Recompilation Research Workspace
Assembles existing public projects as **unmodified upstream submodules**. No new engine code. Nothing here claims GTA VI runs anywhere.
- Status: skeleton only. All upstream data is **UNVERIFIED**; nothing cloned yet (authoring sandbox could not resolve github.com).
- Workflow: ./scripts/add-upstreams.sh <name> -> record-commits.sh -> static-scan.sh -> fill SECURITY_REVIEW.md -> only then build (isolated VM).
- Rules: no game files, assets or keys; no DRM/anti-cheat circumvention; upstream stays pristine (changes go in integrations/ as documented patches).
