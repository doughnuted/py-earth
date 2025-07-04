#ifndef PYE_LONGINTREPR_COMPAT_H
#define PYE_LONGINTREPR_COMPAT_H

#if PY_VERSION_HEX >= 0x030B0000
#include <cpython/longintrepr.h>
#else
#include <longintrepr.h>
#endif

#endif /* PYE_LONGINTREPR_COMPAT_H */
