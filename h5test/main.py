import h5py
import numpy as np

import os
import glob


def main():
    CleanAllHdf5Files()

    CreateDataset()
    Read()

    CreateDataset2()
    Read2()

    RecursiveVisit("hdf5_files/TestFile.hdf5")
    
    Attribute()
    
    PartialIO()
    
    Compression()

    Combine()
    TestCombine()


"""
Delete all hdf5_files.
"""
def CleanAllHdf5Files():
    files = glob.glob('hdf5_files/*.hdf5')
    for f in files:
        os.remove(f)


"""
Demo: Creating a dataset.
"""
def CreateDataset():
    print("\n\n====== CreateDataset")
    file = h5py.File("hdf5_files/TestFile.hdf5", 'a')  # create file
    data_set = file.create_dataset("dataset1", (10, 10), dtype="f")  # create a data set of type float
    data_set[0, 0] = 3.5  # modify a data set
    file.close()  # close object  and file


"""
Demo: Reading a dataset
"""
def Read():
    print("\n\n====== Read")
    file = h5py.File("hdf5_files/TestFile.hdf5", 'r')  # read a file
    data_set = file["dataset1"]
    print("data set shape =", data_set.shape)
    print("data set type =", data_set.dtype)
    print("data set at 0, 0 =", data_set[0, 0])
    file.close()


"""
Demo: Create a dataset using links.
"""
def CreateDataset2():
    print("\n\n====== CreateDataset2")
    file = h5py.File("hdf5_files/TestFile.hdf5", 'a')
    data_set = file.create_dataset("a/b/dataset5", (5, ), dtype="f")
    print("dataset name =", data_set.name)
    file.create_dataset("a/e/dataset3", (13,23,45 ), dtype="f")
    file.create_dataset("f/e/dataset4", (13, ), dtype="f")
    file.close()  # close object  and file

"""
Demo: Read the dataset created in CreateDataset2()
"""
def Read2():
    print("\n\n====== Read2")
    file = h5py.File("hdf5_files/TestFile.hdf5", 'r') 
    print(list(file.keys()))
    print(list(file.values()))
    for name in file:
        print(name)
    print(file["a"].keys())
    file.close()  # close object and file

"""
Demo: Recursivly Visit a file.
    Print all links in this file
"""
def RecursiveVisit(file_name, print_func_name=True):
    if print_func_name:
        print("\n\n====== RecursiveVisit")
    def Action(name):
        print(name)
    file = h5py.File(file_name, 'a') 
    file.visit(Action)
    file.close()  # close object and file

"""
Demo: Test Attributes
"""
def Attribute():
    print("\n\n====== Attribute")
    file = h5py.File("hdf5_files/TestFile.hdf5", 'a')
    data_set = file['dataset1']
    data_set.attrs['added_attribute2'] = 'att2_value'
    print(list(data_set.attrs.keys()))
    print(list(data_set.attrs.values()))
    print(list(data_set.attrs.items()))
    file.close()


"""
Test: PartialIO
"""
def PartialIO():
    print("\n\n====== PartialIO")

    # create some data and store it in a new dataset
    example_data = np.arange(100).reshape((10, 10))
    file = h5py.File("hdf5_files/partial_io.hdf5", "a")
    
    # create one if does not exist
    data_set = file.require_dataset("numbers", data=example_data, dtype=example_data.dtype, shape=example_data.shape)


    # access every other element in the data set
    # very slow access: have to read every single element one at a time
    for x in range(10):
        for y in range(0, 10, 2):
            data_set[x, y] = x + y
    
    print(data_set[:])

    # a faster access    
    print(data_set[:, ::2])
    print(type(data_set[:, ::2]))

    # how to modify data_set[:, ::2]
    a = data_set[:, ::2]
    a[0, 0] = 445
    data_set[:, ::2] = a
    file.close()  # close object  and file


"""
Demo: Compression.
"""
def Compression():
    print("\n\n====== Compression")
    data_size = 1000000
    data = np.arange(data_size)
    file = h5py.File("hdf5_files/uncompressed.hdf5", "a")
    dset = file.create_dataset("big", (data_size,),dtype="int32")
    dset[:] = data
    file.close()
    # ls -hl hdf5_files/uncompressed.hdf5
    # gives file size 3.9M 

    file = h5py.File("hdf5_files/compressed.hdf5", "a")
    dset = file.create_dataset("big", (data_size,),dtype="int32", compression="gzip")
    dset[:]=data
    file.close()
    # ls -hl hdf5_files/compressed.hdf5
    # gives file size 1.4M
    print("done")


"""
Demo: Combine two files.
"""
def Combine():
    print("\n\n====== Combine")
    # the 1st file to combine,
    # it has one dataset called "numbers1".
    file1 = h5py.File("hdf5_files/combine_from_1.hdf5", "a")
    data1 = np.arange(10)
    data_set1 = file1.require_dataset(b"numbers1", data=data1, dtype=data1.dtype, shape=data1.shape)

    # the 2nd file to combine,
    # it has one dataset called "numbers2".
    file2 = h5py.File("hdf5_files/combine_from_2.hdf5", "a")
    data2 = np.arange(10)
    data_set2 = file2.require_dataset(b"numbers2", data=data2, dtype=data2.dtype, shape=data2.shape)

    # method 1: External Link
    # datasets are not copied to Combined1.hdf5
    file_combined_1 = h5py.File("hdf5_files/Combined1.hdf5", "a")
    file_combined_1[b"numbers1"] = h5py.ExternalLink("hdf5_files/combine_from_1.hdf5", b"numbers1")
    file_combined_1[b"numbers2"] = h5py.ExternalLink("hdf5_files/combine_from_2.hdf5", b"numbers2")

    # method 2:h5py.h5o.copy
    # datasets are not copied to Combined1.hdf5
    file_combined_2 = h5py.File("hdf5_files/Combined2.hdf5", "a")
    h5py.h5o.copy(file1.id, b"numbers1", file_combined_2.id, b"numbers1")
    h5py.h5o.copy(file2.id, b"numbers2", file_combined_2.id, b"numbers2")

    file1.close()
    file2.close()
    file_combined_1.close()
    file_combined_2.close()

"""
Test: Check if two combining method works
"""
def TestCombine():
    # Test Method 1
    RecursiveVisit("hdf5_files/Combined1.hdf5", False)
    file1 = h5py.File("hdf5_files/Combined1.hdf5", "a")
    print(list(file1.keys()))
    print(list(file1.values()))
    print(file1[b"numbers1"][5:7])
    print(file1[b"numbers2"][2:7])
    file1.close()
    # ls -hl hdf5_files/Combined1.hdf5
    # gives file size 976B

    # Test Method 2
    RecursiveVisit("hdf5_files/Combined2.hdf5", False)
    file2 = h5py.File("hdf5_files/Combined2.hdf5", "a")
    print(list(file2.keys()))
    print(list(file2.values()))
    print(file2[b"numbers1"][5:7])
    print(file2[b"numbers2"][2:7])
    file2.close()
    # ls -hl hdf5_files/Combined2.hdf5
    # gives file size 2.2K
    
    # RecursiveVisit("Combined2.hdf5")

if __name__ == "__main__":
    main()