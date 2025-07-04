import pytest

def assert_equal(a, b, msg=None):
    assert a == b, msg or f'{a!r} != {b!r}'

def assert_true(x, msg=None):
    assert x, msg or f'{x!r} is not True'

def assert_false(x, msg=None):
    assert not x, msg or f'{x!r} is not False'

def assert_almost_equal(a, b, msg=None, places=7):
    assert a == pytest.approx(b, rel=10**-places), msg or f'{a!r} != {b!r}'

def assert_list_equal(a, b, msg=None):
    assert list(a) == list(b), msg or f'{a!r} != {b!r}'

def assert_not_equal(a, b, msg=None):
    assert a != b, msg or f'{a!r} == {b!r}'

def assert_raises(exc, func, *args, **kwargs):
    with pytest.raises(exc):
        func(*args, **kwargs)
