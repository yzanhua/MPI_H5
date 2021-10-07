This experiments:
1. write a c function that read a h5 data set.
2. provide a python wrapper for this c function.

Usage:
===
1. Modify `H5_DIR` in makefile.
1. Modify  `SCRIPT` in makefile.

1. Modify  `include_dirs` in setup.py.
1. Modify  `extra_link_args` in setup.py.

1. run `make clean`
1. run `make install` to install package. (only once)
1. run `make` to run test.