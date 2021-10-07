H5_DIR=/homes/zhd1108/.hdf5/lib
LD_VAR=LD_LIBRARY_PATH
LD_FALG=$(LD_VAR)=$(H5_DIR)

SCRIPT=tests/test.py  # the "main" python file to run.

.PHONY: all run install clean

all: tests/test.py
	$(LD_FALG) python $(SCRIPT)

install:
	make clean
	pip install -e .

clean:
	pip uninstall z5
	find . -name '__pycache__' -type d -exec rm -rf "{}" +;
	find . -name 'build' -type d -exec rm -rf "{}" +;
	find . -name '*.egg-info' -type d -exec rm -rf "{}" +;
	find . -name '*core*' -type f -delete
	find . -name '*.so' -type f -delete
	find . -name '*.o' -type f -delete
	

