all: module
	echo ""
	python cmath_test.py

install: src/cmod/cmath.c setup.py
	CC=h5pcc pip install -e .
build: cmath.c setup.py
	CC=h5pcc python setup.py build
clean:
	pip uninstall cmod
	rm -rf build cmathExten* dist *.so *.egg-info src/*.egg-info src/cmod/__pycache__ src/cmod/*.so
	

