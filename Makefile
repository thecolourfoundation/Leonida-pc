SHELL := /bin/bash
export PYTHONDONTWRITEBYTECODE := 1
PY := python3
.PHONY: check lint test deps licence submodules secrets

check: lint test licence submodules secrets

lint:
	@for s in scripts/*.sh tests/*.sh; do bash -n "$$s" || exit 1; done
	@$(PY) -c "import ast,sys; [ast.parse(open(f).read(), f) for f in sys.argv[1:]]" $$(find scripts tests tools -name '*.py')
	@echo "lint ok"

test:
	$(PY) -m unittest discover -s tests -v
	bash tests/test_scripts.sh

deps:
	$(PY) -m unittest discover -s tests -p 'test_stdlib_only.py' -v

licence:
	@$(PY) scripts/licence-compat.py | diff -u reports/licence-compat-output.txt - && echo "licence report up to date"
	@bash scripts/check-licenses.sh

submodules:
	@bash scripts/check-submodules.sh && echo "submodule check ok"

secrets:
	@out=$$(bash scripts/static-scan.sh . | sed 's/^wrote //'); \
	if awk '/^## secret-looking strings/{f=1;next} /^## /{f=0} f' "$$out" | grep -q .; then echo "secret-looking strings found in $$out"; exit 1; else echo "no secret-looking strings"; fi

.PHONY: doctor fetch-upstream
doctor:
	@bash scripts/doctor.sh

fetch-upstream:
	@bash scripts/fetch-upstream.sh
