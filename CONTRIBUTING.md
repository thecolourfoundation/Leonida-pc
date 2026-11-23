# Contributing
Never modify upstream/. Changes go in integrations/ as patches or adapter repos, each documented. No game files/keys/assets. No result claims without reproducible evidence.

## Licence rules
No code copied or linked between AnyPS5 (GPL-2.0-only) and Leonida/ReCity (GPL-3.0-or-later). Preserve MIT notices for Xbox2Windows. Never remove upstream copyright/attribution (especially ReCity's relationship to Leonida). Run scripts/licence-compat.py before proposing any integration.

## Restricted licences
Percy6Stars is link-only and licence-isolated: never add it as a submodule without reading its LICENSE (`ALLOW_RESTRICTED=1`), never bundle it in a release, never use it in a commercial distribution without written permission. Apply the same rule to any custom, non-commercial or unlicensed project.

## Quick start
`make doctor` -> `make check` -> `make fetch-upstream`, then use the issue templates (Upstream identity report, Build / test stage result). Open tasks: documentation/PINNED_ISSUE.md, VERIFICATION_CHECKLIST.md. Every PR needs `make check` green and a test for any behaviour change.
