import numpy as np
import time
import sys
a = np.array([1,2,3])
#main benefits - fast,less memory, convenient
l = range(1000)
print("Size of normal list: ",sys.getsizeof(1)*len(l))
b = np.arange(1000)
print("Size of numpy array: ",b.size*b.itemsize)

size = 1000000
l1 = range(size)
l2 = range(size)
a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Python list took: ",(time.time()-start)*1000)
start = time.time()
result = a1+a2
print("Numpy took: ",(time.time()-start)*1000)