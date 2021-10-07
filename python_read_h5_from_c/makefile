# the installation dir of hdf5
HDF5_HOME=/homes/zhd1108/.hdf5

# the "main" python file to run.
SCRIPT=tests/test.py

.PHONY: all run install clean

all: tests/test.py
	python $(SCRIPT)

install:
	HDF5_HOME=$(HDF5_HOME) pip install -e .

clean:
	pip uninstall z5
	find . -name '__pycache__' -type d -exec rm -rf "{}" +;
	find . -name 'build' -type d -exec rm -rf "{}" +;
	find . -name 'dist' -type d -exec rm -rf "{}" +;
	find . -name '*.egg-info' -type d -exec rm -rf "{}" +;
	find . -name '*core*' -type f -delete
	find . -name '*.so' -type f -delete
	find . -name '*.o' -type f -delete
	

