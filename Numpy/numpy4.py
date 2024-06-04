import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
b = a>4
print(b)
print("Something Cool")
print(a[b])
