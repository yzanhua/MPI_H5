import os
from setuptools import setup, Extension, find_packages

os.environ["CC"] = "h5pcc"

# define env variables
HDF5_HOME = None
NUMPY_LIB_HOME="/usr/include/numpy"

# give values to env variables
if "HDF5_HOME" in os.environ:
    HDF5_HOME = os.environ["HDF5_HOME"]

# check env variables not NONE
if HDF5_HOME is None:
    print("HDF5_HOME not defined. Exit.")
    exit(1)
if NUMPY_LIB_HOME is None:
    print("NUMPY_LIB_HOME not defined. Exit.")
    exit(1)

# create sub path
HDF5_INCLUDE = os.path.join(HDF5_HOME, "include")
HDF5_LIB = os.path.join(HDF5_HOME, "lib")

# extension
h5_read_c_module = Extension(name='z5.cread',
                             sources=['src/z5/cread.c'],
                             language="c",
                             include_dirs=[NUMPY_LIB_HOME, HDF5_INCLUDE],
                             library_dirs=[HDF5_LIB],
                             runtime_library_dirs=[HDF5_LIB],
                             extra_compile_args=["-DNDEBUG", "-O3"],
                             extra_link_args=["-lhdf5", "-DNDEBUG", "-O3"],
                             )

setup(
    name="z5",
    version="1.0",
    description="This is my third c extension: call hdf5 for c.",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    ext_modules=[h5_read_c_module]
)
