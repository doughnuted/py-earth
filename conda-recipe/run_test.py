import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pyearth
import pytest

pyearth_dir = os.path.dirname(
    os.path.abspath(pyearth.__file__))
os.chdir(pyearth_dir)
pytest.main([pyearth_dir])
