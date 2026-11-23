# Roadmap
A clone+verify+scan (needs network) -> B licence/security decisions -> C independent upstream builds -> D architecture/compat matrix from evidence -> E classify gaps: reusable / adapter / new engineering (needs approval) / blocked by binaries-hardware / blocked legally.


## Update 2026-11-23
Phase A ordering is now defined in documentation/CLONE_SEQUENCE.md. PS5 portability (AnyPS5) and asset tools are separate tracks. Remote-verification of the 10 non-team-verified repos precedes any clone.

## Update 2026-11-23
Add a licence-resolution step before integration: verify LICENSE texts, enumerate vendored deps, decide the workspace's own licence, and keep AnyPS5 isolated. See VERIFICATION_CHECKLIST.md.

## Update 2026-11-23 (relay 3)
Phase A now covers 13 projects (see CLONE_SEQUENCE.md). Add comparison tracks: Xbox translation layers, BCPack/texture decoding, GPU evidence upgrade (E1 to E2/E3), restricted-licence handling, submodule provenance. No code is copied until licences and provenance are verified.
