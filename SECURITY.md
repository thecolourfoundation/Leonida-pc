# Security policy
- Scope: this repository's scripts and CI. It contains no game files, keys or exploits; report any such content found here immediately and it will be removed.
- Report vulnerabilities privately via GitHub "Report a vulnerability" (Security tab) once the repository is published, or to the maintainer contact listed in the repository profile.
- Upstream projects are untrusted until reviewed: clone with hooks disabled and `--no-checkout`, read build scripts first, build only in an isolated VM (documentation/CLONE_SEQUENCE.md, SECURITY_REVIEW.md).
- Rejected: DRM/anti-cheat bypass, console key or exploit material, leaked or proprietary game data.
- Workflow actions are referenced by version tag; pin to commit SHAs after verifying them online.
