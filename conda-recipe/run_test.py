import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pyearth
import pytest

pyearth_dir = os.path.dirname(os.path.abspath(pyearth.__file__))
pytest.main([pyearth_dir])
