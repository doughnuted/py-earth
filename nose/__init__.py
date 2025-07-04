class SkipTest(Exception):
    pass

from . import tools
__all__ = ['tools', 'SkipTest']
