# Test results (2026-11-23)
Environment: Linux x86_64 (Ubuntu 24.04), 1 CPU, Python 3.12.3, git 2.43.0, GNU make 4.3, bash. No network.
Scope: **our own tooling only**. No upstream project was built or tested.

| Run | Command | Result | Evidence |
|---|---|---|---|
| Baseline (before fixes) | `python3 -m unittest discover -s tests -v`; `bash tests/test_scripts.sh` | 2 failures + 2 errors; 33/34 shell | reports/test-runs/01-baseline-*.txt |
| Regression proof | new self-scan test against script without the exclude fix | 2 FAIL (35 pass / 2 fail), then pass with fix | this commit's session; test in tests/test_scripts.sh |
| After fixes | same commands | 13 tests OK; 37/37 shell | reports/test-runs/02-after-fix-*.txt |
| Full gate | `make check` | exit 0 (lint, tests, licence report, submodules, secret gate) | reports/test-runs/03-make-check.txt |
Not run: GitHub Actions on GitHub runners; every upstream build/test; hardware/GPU tests; any game component.
