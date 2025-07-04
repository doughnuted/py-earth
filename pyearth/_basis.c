/* "pyearth/_basis.pyx":16
 * max_int = sys.maxsize
 *
* import sys             # <<<<<<<<<<<<<<
*/
 * import sys             # <<<<<<<<<<<<<<
 *
 *
 * max_int = sys.maxsize             # <<<<<<<<<<<<<<
 *
  __pyx_t_2 = __Pyx_GetModuleGlobalName(__pyx_n_s_sys); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L1_error)
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_maxsize); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 18, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_max_int, __pyx_t_4) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
