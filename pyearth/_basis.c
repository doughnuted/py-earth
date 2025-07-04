/* "pyearth/_basis.pyx":17
 * max_int = sys.maxsize
 *
 *
 *
*
* # Maximum integer for hashing
* max_int = sys.maxsize
*
* cdef class BasisFunction:
*/
  __pyx_t_2 = __Pyx_GetModuleGlobalName(__pyx_n_s_sys); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_maxsize); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_max_int, __pyx_t_3) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
