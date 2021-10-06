/************************************************************

  This example shows how to create, open, and close a group.

  This file is intended for use with HDF5 Library version 1.8

 ************************************************************/

#include "hdf5.h"
#include "hdf5_hl.h"
#include "stdio.h"
#include "stdlib.h"

#define FILE "../h5files/py_create1.h5"

int main(void)
{
  hid_t file, dset, dcpl; /* Handles */
  herr_t status;
  
  
  // H5Eset_auto(H5E_DEFAULT, NULL, NULL);
  file = H5Fopen(FILE, H5F_ACC_RDONLY, H5P_DEFAULT);
  dset = H5Dopen(file, "numbers", H5P_DEFAULT);
  hid_t dspace = H5Dget_space(dset);

  // get ndims:
  // const int ndims = H5Sget_simple_extent_ndims(dspace);
  // hsize_t dims[ndims];
  // H5Sget_simple_extent_dims(dspace, dims, NULL);

  // get size // H5Dget_type(dset)
  hsize_t dsize = H5Sget_simple_extent_npoints(dspace) * H5Tget_size(H5Dget_type(dset));

  void* buff = malloc(dsize);

  status = H5Dread(dset, H5Dget_type(dset), H5S_ALL, H5S_ALL, H5P_DEFAULT, buff);
  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
    {
      // printf("%ld ", *((long*)(buff + (i * 10 + j) * H5Tget_size(H5Dget_type(dset))) ));
      printf("%d ", ((int*)buff)[i * 10 + j]);
    }
    printf("\n");
  }

  free(buff);
  status = H5Sclose(dspace);
  status = H5Dclose(dset);
  status = H5Fclose(file);
}