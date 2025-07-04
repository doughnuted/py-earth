PYTHON ?= python
CYTHON ?= cython
PYTEST ?= pytest
CYTHONSRC=$(wildcard pyearth/*.pyx)
CSRC=$(CYTHONSRC:.pyx=.c)

inplace: cython
	$(PYTHON) setup.py build_ext -i

all: inplace

cython: $(CSRC)

clean:
	rm -f pyearth/*.c pyearth/*.so pyearth/*.pyc pyearth/test/*.pyc pyearth/test/basis/*.pyc pyearth/test/record/*.pyc

%.c: %.pyx
	$(CYTHON) $<

test: inplace
        $(PYTEST) -s pyearth/test

test-coverage: inplace
        $(PYTEST) --cov=pyearth --cov-report=html

verbose-test: inplace
        $(PYTEST) -sv pyearth/test

conda:
	conda-build conda-recipe
