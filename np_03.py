import numpy as np

x = np.array([1,2,3,4])
# print(x[0])

for i in x:
    print(i)

y = np.array([[1,2,3,4], [5,6,7,8]])
print("size", y[0].size)
print(y[0][3])
print(y[0,3])

z = np.array([[[1,2],[3,4]], [[1,2],[3,4]]])
print(z[0,0,1])


# Indexing
# 0, 1, 2, 3, 4, ....

# Negative Indexing
# -1, -2, -3, -4, ....