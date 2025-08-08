import numpy as np


#question: 
q1 = np.array([9,3,2,5,1,6])
print('initial array is: ', q1)
print('sorted array is: ',np.sort(q1))
print('initial array is not change: ',q1)
print('sorted array is: ', q1)

print('sorted array in descending order is: ', np.sort(q1)[::-1])
# , q1.sort(1)

a = np.array([[6,2,3],[4,9,2],[1,5,8]])

print('sorted arry default is: ',np.sort(a))#default is along axis 1
print('sorted arry along axis 0 is: ',np.sort(a, axis=0))
print('sorted arry along axis 1 is: ',np.sort(a, axis=1))

print('fullsorting of the array is: ', np.sort(a, axis=None))

print('sorted to 1D without axis is: ', np.sort(a.flatten()).reshape(3,3))