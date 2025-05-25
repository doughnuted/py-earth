import pyearth
import pytest
import os

# It's generally better to run pytest from the repository root or let conda handle
# the test execution path. However, to closely mimic the previous behavior of
# running tests from within the pyearth directory, we'll keep the chdir.
# Pytest will discover tests in the 'pyearth' directory.
pyearth_dir = os.path.dirname(
    os.path.abspath(pyearth.__file__))
os.chdir(pyearth_dir)
# Ensure pytest runs on the pyearth module itself
# The return code of pytest.main will be used by conda build to determine success/failure
# Adding '-s' and '-v' for similar verbosity to "nosetests -s -v"
# We specify 'pyearth' as the target directory for pytest to find tests.
# Since we chdir into pyearth_dir, and pyearth tests are in pyearth/test,
# pytest should find them automatically. If not, we might need to specify 'test'.
# Let's assume pytest's default discovery from the current directory (pyearth_dir) works.
# If tests are in a subfolder like 'tests' directly under pyearth_dir, it would be 'tests'.
# Given the project structure, tests are in 'pyearth/test', so running pytest
# from 'pyearth' directory should find 'test' subdirectory.
# If pyearth_dir is /path/to/pyearth, then running pytest in /path/to/pyearth
# should find tests in /path/to/pyearth/test
# The original `nose.run(module=pyearth)` likely means it ran tests found *within* the pyearth package.
# So, running `pytest .` from within the pyearth directory should be equivalent.
# Or, more explicitly, `pytest pyearth` from the parent of pyearth_dir.
# Since we chdir into pyearth_dir, `pytest .` or just `pytest` might be enough.
# Let's try with `pytest . --pyargs pyearth` to be safe, or just `pytest .`
# After chdir to pyearth_dir, tests are in ./test
# pytest should discover ./test
exit_code = pytest.main(['-s', '-v', 'test'])
exit(exit_code)
