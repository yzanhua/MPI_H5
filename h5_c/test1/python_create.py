import h5py as h5
import numpy as np
import os

DATA_SET_FOLDER = "../h5files"

def OpenFile(file_name, mode):
    file_path = os.path.join(DATA_SET_FOLDER, file_name)
    file = h5.File(file_path, mode)
    return file

def main():
    example_data = np.arange(100,dtype="int32").reshape((10, 10))
    
    with OpenFile("py_create1.h5", "a") as file:
        data_set = file.require_dataset("numbers", data=example_data, dtype=example_data.dtype, shape=example_data.shape)
    

if __name__ == "__main__":
    main()
