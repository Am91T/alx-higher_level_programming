#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list
 * @p: a pointer to a pyobj
 * Return: is a void func
 */
void print_python_list_info(PyObject *p) {
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); ++i) {
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
