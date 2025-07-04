*         Return the weighted sum of squared errors for the linear least squares problem
 *         ``self.sse_`` stores this quantity and is updated in ``update``.
 *         return self.omega - np.dot(self.theta, self.theta)             # <<<<<<<<<<<<<<
  __pyx_t_9 = __pyx_PyFloat_AsDouble(__pyx_t_4); if (unlikely((__pyx_t_9 == ((npy_float64)-1)) && PyErr_Occurred())) __PYX_ERR(0, 169, __pyx_L1_error)
*         Return the weighted sum of squared errors for the linear least squares problem
static char __pyx_doc_7pyearth_12_knot_search_26SingleOutcomeDependentData_4sse[] = "\n        Return the weighted sum of squared errors for the linear least squares\n        problem represented by Q_t, y, and w.  `self.sse_` stores the same\n        quantity.\n        ";
