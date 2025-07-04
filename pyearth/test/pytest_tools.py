import pytest
from numpy.testing import assert_almost_equal, assert_array_almost_equal


def assert_equal(a, b):
    assert a == b


def assert_true(x):
    assert x


def assert_false(x):
    assert not x


def assert_list_equal(a, b):
    assert list(a) == list(b)


def assert_not_equal(a, b):
    assert a != b


def assert_raises(exc, func, *args, **kwargs):
    with pytest.raises(exc):
        func(*args, **kwargs)
