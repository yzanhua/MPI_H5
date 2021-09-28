This folder contains codes for testing:
1. calling c functions from python using `ctype`.
2. calling c functions from python using `pymodule`.


Test - ctypes:
===
Run:
1. Enter the folder `ctype_test`.
2. Run `make` to compile `spam.c` to `spam.so`.
3. Run `python test.py`.

Res: (adding 1000000+1 numbers)

1. my_c_time: 0.00043463706970214844
2. builtin_sum_time: 0.004506111145019531
3. np_sum_time: 0.0006175041198730469
4. pyloop_time: 0.05648350715637207

Test - pymodules:
===
Run:
1. Enter the folder `pymodule_test`.
1. Run `make`.

Res: (adding 1000000+1 numbers)
1. myCmath time: 0.004016399383544922
2. python time: 0.10833501815795898
3. python builtin time: 0.004462480545043945
4. numpy time: 0.0005686283111572266

TODO: -O3 seems not working.
