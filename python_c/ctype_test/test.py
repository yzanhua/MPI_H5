import ctypes
import time
import numpy as np


# create data
NUM=1000000+1
data = [i for i in range(NUM)]

# load c_modules
spam = ctypes.CDLL("./spam.so")

# convert data to ctypes-readable format
c_list = (ctypes.c_long * NUM)(*data)

# sum - by ctypes
spam.sum.restype = ctypes.c_long
start = time.time()
c_sum = spam.sum(c_list, len(c_list))
end = time.time()
c_time = end - start


# sum - by python built in
start = time.time()
builtin_sum = sum(data)
end = time.time()
builtin_time = end - start

# sum - python loop
pyloop_sum = 0
start = time.time()
for x in data:
    pyloop_sum += x
end = time.time()
pyloop_time = end - start

# sum - by numpy
data = np.array(data)
start = time.time()
np_sum = np.sum(data)
end = time.time()
np_time = end - start

print(c_sum, c_time)
print(builtin_sum, builtin_time)
print(np_sum, np_time)
print(pyloop_sum, pyloop_time)
