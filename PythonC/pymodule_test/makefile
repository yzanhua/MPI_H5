# PYTHON3C=$(shell pkg-config --cflags --libs python3)
# all: compile

# compile: factorial.c
# 	gcc spam.c ${PYTHON3C} -o spam
# run: spam
# 	./spam
# clean:
# 	rm -f spam
all: module
	echo ""
	python cmath_test.py

module: cmath.c setup.py
	python setup.py build
	yes | cp -f build/*/*.so .
