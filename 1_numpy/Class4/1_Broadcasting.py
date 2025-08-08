import numpy as np

a = np.array([[0,1,2]])

print(a.shape)  # Output: (4,)
print(a.ndim)   # Output: 1 (1D array)

b = np.array([[0], [10], [20], [30]])

print(a + b)

a = np.arange(0,40,10)

print(a)
print(np.vstack((a,a,a)))
print(np.hstack((a,a,a)))

print(np.tile(a,(3,2)))

print(np.array([1,2,3,4,5])+np.arange(12).reshape(4,3))