import numpy as np
a = np.array([[6,7,8],[1,2,3],[9,3,2]])
print(a[1,2])
print(a[0:2,2])
#array iteration
print("Array Iteration")
for cell in a.flat:
    print(cell)

b = np.arange(6).reshape(3,2)
c = np.arange(6,12).reshape(3,2)
d = np.vstack((b,c)) #stacking two array on top of each other
print("VerticalStack:",d)
print("HorizontalStack: ",np.hstack((b,c)))

e = np.arange(30).reshape(2,15)
print(e)
print("Horizontal Array Splitting")
print(np.hsplit(e,3))
print("Vertical Array Spliting") 
print(np.vsplit(e,2))
