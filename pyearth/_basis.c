static const char __pyx_k_iteritems[] = "items";
static const char __pyx_k_itervalues[] = "values";
 *         for d in intermediate.values():
 *             for var, lst in d.items():
 *         for vars, bfs in anova.items():
 *         for vars, bfs in anova.items():
 *         for vars, bfs in anova.items():             # <<<<<<<<<<<<<<
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%s'", "items");
  __pyx_t_5 = __Pyx_dict_iterator(__pyx_v_anova, 1, __pyx_n_s_items, (&__pyx_t_3), (&__pyx_t_4)); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 989, __pyx_L1_error)
 *         for vars, bfs in anova.items():
 *         for vars, bfs in anova.items():
 *         for vars, bfs in anova.items():
 *         for d in intermediate.values():
 *         for d in intermediate.values():
 *             for var, lst in d.items():
 *         for d in intermediate.values():             # <<<<<<<<<<<<<<
 *             for var, lst in d.items():
  __pyx_t_6 = __Pyx_dict_iterator(__pyx_v_intermediate, 1, __pyx_n_s_values, (&__pyx_t_2), (&__pyx_t_4)); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 998, __pyx_L1_error)
 *         for d in intermediate.values():
 *             for var, lst in d.items():             # <<<<<<<<<<<<<<
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%s'", "items");
    __pyx_t_5 = __Pyx_dict_iterator(__pyx_v_d, 0, __pyx_n_s_items, (&__pyx_t_14), (&__pyx_t_7)); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 999, __pyx_L1_error)
 *         for d in intermediate.values():
 *             for var, lst in d.items():
 *             for var, lst in d.items():
        if (strcmp(name, "items") == 0) pp = &py_items;
        else if (strcmp(name, "values") == 0) pp = &py_values;
