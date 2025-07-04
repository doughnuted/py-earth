'''
Created on Feb 16, 2013

@author: jasonrudy
'''
from .earth import Earth
import numpy as np
_alias_map = {'int': 'int_', 'float': 'float64', 'bool': 'bool_'}
for _name, _target in _alias_map.items():
    if not hasattr(np, _name) and hasattr(np, _target):
        setattr(np, _name, getattr(np, _target))

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
