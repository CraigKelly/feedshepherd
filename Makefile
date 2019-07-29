BASEDIR=$(CURDIR)
SAMPLEDIR=$(BASEDIR)/samples

PACKAGE=feedshepherd

SOURCES := $(shell find $(PACKAGE) -type f)

.PHONY: main
main:
	@echo "TODO: anything"

.PHONY: setup
setup:
	pipenv install

.PHONY: dev-setup
dev-setup: setup
	pipenv run python -m pip install ipython

.PHONY: dev-shell
dev-shell:
	pipenv run ipython

.PHONY: clean-setup
clean-setup:
	pipenv --rm || true
	rm -f Pipfile.lock

.PHONY: relock-setup
relock-setup: clean-setup setup
	@echo "You should check git status"

.PHONY: clean
clean:
	@echo "TODO: clean functionality"
