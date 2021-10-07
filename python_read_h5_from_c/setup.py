import os
from setuptools import setup, Extension, find_packages

os.environ["CC"] = "h5pcc"

h5_read_c_module = Extension(name='z5.cread',
                             sources=['src/z5/cread.c'],
                             language="c",
                             include_dirs=["/usr/include/numpy",
                                           "/home/zanhua/.hdf5/include"],
                             extra_compile_args=["-DNDEBUG", "-O3"],
                             extra_link_args=[
                                 "-L/homes/zhd1108/.hdf5/lib", "-l:libhdf5.so"],
                             )


setup(
    name="z5",
    version="1.0",
    description="This is my third c extension: call hdf5 for c.",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    ext_modules=[h5_read_c_module]
)
