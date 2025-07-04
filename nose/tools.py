from numpy.testing import assert_almost_equal
import contextlib

__all__ = [
    'assert_true', 'assert_false', 'assert_equal', 'assert_not_equal',
    'assert_list_equal', 'assert_almost_equal', 'assert_raises'
]


def assert_true(expr, msg=None):
    assert bool(expr), msg or "expression is not true"

def assert_false(expr, msg=None):
    assert not expr, msg or "expression is not false"

def assert_equal(a, b, msg=None):
    assert a == b, msg or f"{a!r} != {b!r}"

def assert_not_equal(a, b, msg=None):
    assert a != b, msg or f"{a!r} == {b!r}"

def assert_list_equal(a, b, msg=None):
    assert list(a) == list(b), msg or f"{a!r} != {b!r}"

class _AssertRaisesContext:
    def __init__(self, exc):
        self.exc = exc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            raise AssertionError(f"{self.exc} was not raised")
        return issubclass(exc_type, self.exc)

def assert_raises(exc, *args, **kwargs):
    if not args:
        return _AssertRaisesContext(exc)
    func = args[0]
    try:
        func(*args[1:], **kwargs)
    except exc:
        return
    raise AssertionError(f"{exc} was not raised")
