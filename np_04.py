import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
# x[start:end]
print(x[0:4])
print(x[-5:-2])

# with step size
print(x[0:8:2])
print(x[0::3])
print(x[::2])

# Index 0 to Index 4
print(x[:4])
print(x[::4])

# Index 04 to End of the Array
print(x[4:])
print(x[4::])


# 02 Dimensional Array
y = np.array([[1,2,3,4], [5,6,7,8]])
print(y[0,1::]) 
print(y[:,3])