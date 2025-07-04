import os
import pyearth
import pytest

pyearth_dir = os.path.dirname(
    os.path.abspath(pyearth.__file__))
os.chdir(pyearth_dir)
pytest.main(["-s", "-v"])
