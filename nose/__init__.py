import sys
from types import ModuleType
from unittest import SkipTest

# Create a tools module providing common nose assertion helpers
_tools = ModuleType('nose.tools')

def assert_equal(a, b, msg=None):
    assert a == b, msg or f"{a!r} != {b!r}"

def assert_true(expr, msg=None):
    assert bool(expr), msg or f"{expr!r} is not True"

def assert_false(expr, msg=None):
    assert not bool(expr), msg or f"{expr!r} is not False"

def assert_almost_equal(a, b, places=7, msg=None):
    assert round(abs(a - b), places) == 0, msg or f"{a!r} !~= {b!r}"

def assert_list_equal(a, b, msg=None):
    assert list(a) == list(b), msg or f"{a!r} != {b!r}"

def assert_raises(exc, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exc:
        return
    except Exception as e:
        assert False, f"expected {exc}, got {type(e)}"
    else:
        assert False, f"expected {exc} to be raised"

def assert_not_equal(a, b, msg=None):
    assert a != b, msg or f"{a!r} == {b!r}"

# attach functions to tools module
for name, obj in list(locals().items()):
    if name.startswith('assert_'):
        setattr(_tools, name, obj)

sys.modules[__name__ + '.tools'] = _tools

__all__ = ['SkipTest', 'tools']
