import numpy as np

# zero dimensional array
a = np.array(1)
print(a)
print(a.ndim)

# one dimensional array
x = np.array([1,2,3,4])
print(x)
print(x.ndim) # dimension of array

# two dimensional array
y = np.array([[1,2,3,4],[5,6,7,8]])
print(y)
print(y.ndim)

# three dimensional array
z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(z)
print(z.ndim)

b = np.array([1,2,3,4], ndmin=5)
print(b)
print(b.ndim)