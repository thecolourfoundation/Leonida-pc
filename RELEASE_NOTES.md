# v0.1.0-rc1 (tooling release candidate)
**Scope:** workspace tooling, tests and CI only. No upstream built, no binaries, **no playable or bootable GTA VI**.

Included: manifest-driven upstream vetting scripts (guards for unverified and restricted-licence repos), licence-combination checker, passive static scan, provenance scripts, 13 Python + 37 shell offline tests, Makefile, CI workflow, research docs.
Fixed during testing: static-scan wrote no report outside repo root; static-scan read its own output; licence-compat was not importable.
Evidence: reports/test-runs/ (baseline failures, after-fix passes, `make check`).
Known limits: CI workflow not yet run on GitHub; all upstream facts are second-hand documentation; LICENSE for original files is proposed MIT pending owner confirmation.
