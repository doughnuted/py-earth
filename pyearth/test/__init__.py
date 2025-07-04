import pytest
import pyearth
if not pyearth.HAS_EXT:
    pytest.skip("Compiled extensions not available", allow_module_level=True)
