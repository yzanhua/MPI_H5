all: module
	echo ""
	python cmath_test.py

module: cmath.c setup.py
	python setup.py build
	yes | cp -f build/*/*.so .
