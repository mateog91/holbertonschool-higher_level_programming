#include <Python.h>

/**
 * print_python_list_info - unction that prints some basic info about Python lists.
 * @p: pointer to PyObject
 * 
 */
void print_python_list_info(PyObject *p)
{
	int i, size;
	PyListObject *list;

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %i\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %li\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}