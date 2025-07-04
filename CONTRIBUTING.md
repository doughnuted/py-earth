# Contributing to py-earth

Thank you for considering contributing to py-earth!

## Building Cython extensions

The test suite requires the Cython extensions to be compiled. Before running the
tests, build the extensions in place with one of the following commands:

```bash
pip install -e .
# or
python setup.py build_ext --inplace
```

After the extensions are built you can run the test suite, e.g. with `make test`
or directly using `nosetests`.
