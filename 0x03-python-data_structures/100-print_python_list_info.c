#include <Python.h>

/**
 * print_python_list_info - a C function that prints some
 * basic info about Python lists.
 * @p: PyObject list
*/
void print_python_list_info(PyObject *p)
{
	int py_alloc, py_sz, x;
	PyObject *ptr;

	py_sz = Py_SIZE(p);
	py_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	pritnf("[*] Allocated = %d\n", alloc);

	for (x = 0; 0 < py_sz; x++)
	{
		printf("Element %d: ", x);

		ptr = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(ptr)->tp_name);
	}
}

