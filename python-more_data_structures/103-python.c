#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size;
    Py_ssize_t i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);

    printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);

    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02x", (unsigned char)bytes->ob_sval[i]);

    printf("\n");
}


void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size;
    Py_ssize_t allocated;
    Py_ssize_t i;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
        return;

    list = (PyListObject *)p;

    size = list->ob_base.ob_size;
    allocated = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = list->ob_item[i];

        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
        {
            printf("bytes\n");
            print_python_bytes(item);
        }
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyList_Check(item))
            printf("list\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("%s\n", item->ob_type->tp_name);
    }
}
