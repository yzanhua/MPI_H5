import ctypes

spam = ctypes.CDLL("./spam.so")

li = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
a = spam.sum(li, len(li))
print(a)
