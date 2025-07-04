cimport numpy as cnp
ctypedef cnp.float64_t FLOAT_t
# ``cnp.int_t`` was removed from NumPy's C API. ``cnp.int64_t`` maps to the
# standard 64-bit integer type and works as a drop-in replacement.
ctypedef cnp.int64_t INT_t
ctypedef cnp.intp_t INDEX_t
ctypedef cnp.uint8_t BOOL_t
