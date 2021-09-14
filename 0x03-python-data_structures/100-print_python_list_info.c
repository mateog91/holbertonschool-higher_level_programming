#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list_info(PyObject *p)
{
    printf("The type is %s\n", Py_TYPE(p))
}
