import numpy as np
#two dimensional array
a = np.array([[3,4],[1,2],[5,6]])
print("Dimensions: ",a.ndim) #dimensions of a array
print("ItemSize: ",a.itemsize) #size of a single element
print("Datatype:",a.dtype) #data type of array
b = np.array([[1,2],[3,4]],dtype=np.float64) #initialize array of float dtype
print("Size:",a.size) #total elements
print("Shape: ",a.shape) #shape of array
c = np.zeros((3,4)) #array of zeros of shape (3,4)
print("Zeros: ",c)
d = np.ones((3,4)) #array of ones of shape(3,4)
e = np.arange(1,5) #all element in range (1,5)
f = np.arange(1,5,2) #[1,3]
g = np.linspace(1,5,10) #10 elements linearly spaced from 1-5 range
print("Linespace: ",g)
print("Reshape:",a.reshape(2,3)) #reshapes array to desired dimension, as long as it is computable
print("Ravel: ",a.ravel())
print("Min: ",a.min()) #minimum element
print("Max: ",a.max()) #maximum element
print("Sum: ",a.sum()) #sum all elements
print("Axis0: ",a.sum(axis=0)) #axis0 is columns
print("Axis1: ",a.sum(axis=1)) #axis1 is rows
print("Root: ",np.sqrt(a)) #square root of all elements
print("StandardDeviation:",np.std(a)) #standard deviation of all elements
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("Sum of 2 arrays: ",a+b)
#you can also do a*b, a/b, a-b.
print("Matrix Multiplication: ",a.dot(b)) #if single dimension then normal dot product, if not then multiplication of matrix

