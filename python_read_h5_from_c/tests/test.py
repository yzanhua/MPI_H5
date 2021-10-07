import z5.z5read as z
import numpy as np
import h5py
import os


dir_path = os.path.dirname(os.path.realpath(__file__))


def GetFilePath(file_name):
    return os.path.join(dir_path, "h5files", file_name)


def GetH5File(file_name):
    file_path = GetFilePath(file_name)
    return h5py.File(file_path, "a")


def GetDataSet(h5file, dset_name, data):
    return h5file.require_dataset(dset_name, data=data, dtype=data.dtype, shape=data.shape)


def main():
    f_name = "test.hdf5"
    dset_name = "dset2"
    dsize_root = 10
    data = np.arange(dsize_root * dsize_root * dsize_root, dtype="int32")
    data.resize((dsize_root, dsize_root, dsize_root))

    with GetH5File(f_name) as file:
        dset = GetDataSet(file, dset_name, data)

    data = z.read_dataset(GetFilePath(f_name), dset_name)
    print(type(data))
    print(data.shape)
    print(data[9, 9, 9])


if __name__ == "__main__":
    main()
