import sys
import os

# Ensure the local package can be imported when running tests from the
# conda recipe directory.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pyearth

# Basic sanity check that the main estimator is available. The full test
# suite is executed separately via ``pytest``.
assert hasattr(pyearth, "Earth")
