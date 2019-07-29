BASEDIR=$(CURDIR)
SAMPLEDIR=$(BASEDIR)/samples

PACKAGE=feedshepherd

SOURCES := $(shell find $(PACKAGE) -type f)

.PHONE: main
main:
	@echo "TODO: anything"
