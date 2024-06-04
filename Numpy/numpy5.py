import numpy as np
a =  np.arange(12).reshape(3,4)
#array iteration
print("Normal Iteration")
for cell in a.flatten():
    print(cell)

#using nditer
print("\nNditer C")
for x in np.nditer(a,order='C'):
    print(x)

print("\nNditer F")
for x in np.nditer(a,order='F'):
    print(x)

print("\nExternal Loop Flag")
for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)

print("\nop_flag readwrite")
for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x
print(a)

b = np.arange(3,15,4).reshape(3,1)

#Iterating 2 array simultaneously
print("\nIterating 2 array simul.")
for x,y in np.nditer([a,b]):
    print(x,y)