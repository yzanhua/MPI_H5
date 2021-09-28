import myCmath
import time, random
random.seed()

NUM=10000

# create NUM random integers
theList = []
for i in range(NUM):
    theList.append(random.randint(0, 1000))

# sum by cmath
start = time.time()
res = myCmath.sum(theList)
end = time.time()
print("myCmath res:", res)
print("myCmath time:", end - start)

# sum by python
start = time.time()
res = 0
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