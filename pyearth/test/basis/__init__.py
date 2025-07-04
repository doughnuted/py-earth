import pickle
import os
from numpy.testing import assert_equal

import numpy

from pyearth._basis import Basis, ConstantBasisFunction, HingeBasisFunction, \
    LinearBasisFunction, SmoothedHingeBasisFunction

numpy.random.seed(0)
