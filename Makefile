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

.PHONY: relock-setup
relock-setup:
	pipenv --rm || true
	rm -f Pipfile.lock
	pipenv install
	@echo "You should check git status"

.PHONY: clean
clean:
	@echo "TODO: clean functionality"
