import os
import pytest
try:
    import pyearth
except Exception:
    pytest.skip("pyearth package not available", allow_module_level=True)
if not getattr(pyearth, "HAS_EXT", False):
    pytest.skip("compiled extensions missing", allow_module_level=True)
import nose

pyearth_dir = os.path.dirname(
    os.path.abspath(pyearth.__file__))
os.chdir(pyearth_dir)
nose.run(module=pyearth)
