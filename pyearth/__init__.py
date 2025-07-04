'''
Created on Feb 16, 2013

@author: jasonrudy
'''
try:
    from .earth import Earth
except Exception:  # compiled extensions likely missing
    Earth = None
HAS_EXT = Earth is not None

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
