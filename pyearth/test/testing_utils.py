import os
import sys
from functools import wraps
from distutils.version import LooseVersion

import pytest
from numpy.testing import assert_almost_equal

def if_environ_has(var_name):
    """Decorator that skips the test when the given environment variable is missing."""

    def if_environ(func):
        @wraps(func)
        def run_test(*args, **kwargs):
            if var_name in os.environ:
                return func(*args, **kwargs)
            pytest.skip(f"Only run if {var_name} environment variable is defined.")

        return run_test

    return if_environ

def if_platform_not_win_32(func):
    @wraps(func)
    def run_test(*args, **kwargs):
        if sys.platform == 'win32':
            pytest.skip('Skip for 32 bit Windows platforms.')
        return func(*args, **kwargs)

    return run_test
            
def if_sklearn_version_greater_than_or_equal_to(min_version):
    '''
    Test decorator that skips test unless sklearn version is greater than or
    equal to min_version.
    '''
    def _if_sklearn_version(func):
        @wraps(func)
        def run_test(*args, **kwargs):
            import sklearn
            if LooseVersion(sklearn.__version__) < LooseVersion(min_version):
                pytest.skip('sklearn version less than %s' % str(min_version))
            return func(*args, **kwargs)
        return run_test
    return _if_sklearn_version


def if_statsmodels(func):
    """Test decorator that skips test if statsmodels is not installed."""

    @wraps(func)
    def run_test(*args, **kwargs):
        pytest.importorskip('statsmodels')
        return func(*args, **kwargs)

    return run_test


def if_pandas(func):
    """Test decorator that skips test if pandas is not installed."""

    @wraps(func)
    def run_test(*args, **kwargs):
        pytest.importorskip('pandas')
        return func(*args, **kwargs)

    return run_test

def if_sympy(func):
    """Test decorator that skips test if sympy is not installed."""

    @wraps(func)
    def run_test(*args, **kwargs):
        pytest.importorskip('sympy')
        return func(*args, **kwargs)

    return run_test
    


def if_patsy(func):
    """Test decorator that skips test if patsy is not installed."""

    @wraps(func)
    def run_test(*args, **kwargs):
        pytest.importorskip('patsy')
        return func(*args, **kwargs)

    return run_test


def assert_list_almost_equal(list1, list2):
    for el1, el2 in zip(list1, list2):
        assert_almost_equal(el1, el2)


def assert_list_almost_equal_value(list, value):
    for el in list:
        assert_almost_equal(el, value)
