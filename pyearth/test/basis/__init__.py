import pickle
import os
import pytest

import numpy

from pyearth._basis import Basis, ConstantBasisFunction, HingeBasisFunction, \
    LinearBasisFunction, SmoothedHingeBasisFunction

numpy.random.seed(0)
