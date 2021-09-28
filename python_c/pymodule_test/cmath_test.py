import myCmath
import time, random
import numpy as np

random.seed()

NUM=1000000+1

# create NUM random integers
theList = [i for i in range(NUM)]

# sum by cmath
start = time.time()
res = myCmath.sum(theList)
end = time.time()
print("myCmath res:", res)
print("myCmath time:", end - start)

# sum by python
res = 0
start = time.time()
for i in range(NUM):
    res += theList[i]
end = time.time()
print("python res:", res)
print("python time:", end - start)

# sum by python built-in sum:
start = time.time()
res = sum(theList)
end = time.time()
print("python builtin res:", res)
print("python builtin time:", end - start)

# sum by python built-in sum:
np_data = np.array(theList)
start = time.time()
res = np.sum(np_data)
end = time.time()
print("numpy res:", res)
print("numpy time:", end - start)