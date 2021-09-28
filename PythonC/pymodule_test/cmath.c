#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

// helper function to calculate factorial
int factorial(int n)
{
    int res = 1;
    for (int i = 1; i <= n; i++)
        res *= i;
    return res;
}

// define and implement method - factorial
static PyObject *factorial_wrapper(PyObject *self, PyObject *args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    int result = factorial(n);
    return Py_BuildValue("i", result);
}

// define and implememt method - sum
static PyObject *sum_wrapper(PyObject *self, PyObject *args)
{
    PyObject *int_list; // the list of integers
    PyObject *item;     // will store each integers
    int list_length;
    PyObject *(*get_item_ptr)(PyObject *, Py_ssize_t);
    long sum = 0;

    if (!PyArg_ParseTuple(args, "O", &int_list))
        return NULL;

    // check if it is a tuple or List
    if (PyTuple_Check(int_list))
        get_item_ptr = PyTuple_GetItem;
    else if (PyList_Check(int_list))
        get_item_ptr = PyList_GetItem;
    else
    {
        PyErr_SetString(PyExc_TypeError, "should be a tuple or list.");
        return NULL;
    }

    // check length
    list_length = PyObject_Length(int_list);
    if (list_length < 0)
        return NULL;

    for (int i = 0; i < list_length; i++)
    {
        // get then item
        item = get_item_ptr(int_list, i);

        // add to sum if of type - Long
        if (PyLong_Check(item))
            sum += PyLong_AsLong(item);
        else
        {
            PyErr_SetString(PyExc_TypeError, "Non-Integer valule contained in list.");
            return NULL;
        }
    }
    return Py_BuildValue("l", sum);
}

// specify all methods of the module
static PyMethodDef cmath_methods[] = {
    {"factorial", factorial_wrapper, METH_VARARGS, "Calculate the factorial of n."},
    {"sum", sum_wrapper, METH_VARARGS, "Calculate the sum of the list or tuple."},
    {NULL, NULL, 0, NULL} // should end with {NULL,....., NULL}
};

// define module
static PyModuleDef cmath_module = {
    PyModuleDef_HEAD_INIT,
    "myCmath", "factorial and sum", // name, explanation
    -1,
    cmath_methods // methods here
};

// Create the Module
// This should be the only non static method (except the helper funcs)
PyMODINIT_FUNC PyInit_myCmath(void)
{
    return PyModule_Create(&cmath_module);
}
