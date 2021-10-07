#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <arrayobject.h>

#include "hdf5.h"
#include "hdf5_hl.h"

#include <stdlib.h>
#include <stdio.h>

// define and implememt method - read_dataset
static PyObject *read_wrapper(PyObject *self, PyObject *args)
{
    const char *file_name, *dset_name;
    if (!PyArg_ParseTuple(args, "ss", &file_name, &dset_name))
    {
        PyErr_SetString(PyExc_TypeError, "Parsing two strings fails.");
        return NULL;
    }
    herr_t status;

    hid_t file = H5Fopen(file_name, H5F_ACC_RDONLY, H5P_DEFAULT);
    hid_t dset = H5Dopen(file, dset_name, H5P_DEFAULT);
    hid_t dspace = H5Dget_space(dset);

    // get ndims:
    const int ndims = H5Sget_simple_extent_ndims(dspace);
    hsize_t dims[ndims];
    H5Sget_simple_extent_dims(dspace, dims, NULL);

    // get needed size
    hsize_t dsize = H5Sget_simple_extent_npoints(dspace) * H5Tget_size(H5Dget_type(dset));
    void *buff = malloc(dsize);
    status = H5Dread(dset, H5Dget_type(dset), H5S_ALL, H5S_ALL, H5P_DEFAULT, buff);

    PyArrayObject *result;
    result = (PyArrayObject *)PyArray_SimpleNewFromData(ndims, dims, PyArray_INT32, buff);

    status = H5Sclose(dspace);
    status = H5Dclose(dset);
    status = H5Fclose(file);

    return PyArray_Return(result);
}

// specify all methods of the module
static PyMethodDef cread_methods[] = {
    {"read_dataset", read_wrapper, METH_VARARGS, "method: read an hdf5 file dataset and return as numpy.."},
    {NULL, NULL, 0, NULL} // should end with {NULL,....., NULL}
};

// define module
static PyModuleDef cread_module = {
    PyModuleDef_HEAD_INIT,
    "cread", "module: read an hdf5 file dataset and return as numpy.", // name, explanation
    -1,
    cread_methods // methods here
};

// Create the Module
// This should be the only non static method (except the helper funcs)
PyMODINIT_FUNC PyInit_cread(void)
{
    import_array();
    return PyModule_Create(&cread_module);
}
