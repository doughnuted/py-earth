PYTHON ?= python
CYTHON ?= cython
TEST_RUNNER ?= pytest
CYTHONSRC=$(wildcard pyearth/*.pyx)
CSRC=$(CYTHONSRC:.pyx=.c)

inplace: cython
	$(PYTHON) setup.py build_ext --inplace --cythonize

all: inplace

cython: $(CSRC)

clean:
	rm -f pyearth/*.c pyearth/*.so pyearth/*.pyc pyearth/test/*.pyc pyearth/test/basis/*.pyc pyearth/test/record/*.pyc

%.c: %.pyx
	$(CYTHON) $<

test: inplace
	$(TEST_RUNNER) -s pyearth

test-coverage: inplace
	$(TEST_RUNNER) --cov=pyearth --cov-report=html pyearth

verbose-test: inplace
	$(TEST_RUNNER) -vv pyearth

conda:
	conda-build conda-recipe
