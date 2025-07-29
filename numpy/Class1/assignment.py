import numpy as np

#1 print even and odd numbers in a range
print(np.arange(22,71,2))
print(np.arange(21,72,2))

#2 convert int array to float
arr = np.array([10,20,30,40,50])
print(arr.astype('float64'))

#3 print range of array
print(np.arange(10))
print(np.arange(10)[2:5])

#4 change sign of values in array on condition
x = np.array([-5,9,20,25,-3,5,16,10,-8])
x[(x >= -5) & (x <= 15)] *= -1
print(x)

#7 array with start, length, step
print('start:5, length:10, step:3 ',np.arange(5,5+10* 3, 3))


#7 array with start, end, step and rounded to 2 decimal places
print('start:5, end:7, step:0.5 ',np.arange(5,7,0.5).round(2))

#9 Transpose output
a = np.array([[34, 28,55], [8, 56, 3], [77, 87, 19]])
print(a.transpose()[-2,-2])

#2 array equality
a = np.array([100,200,300,400])
b = np.array([300,200,100,400])
print(a == b)

#3 accessing with multiple indices
a = np.array([10,12,15,17,2,5,4,6])
print( a[[0,2,4,6]],a[::2])

#4 change values at specific indices with range step
a = np.array([1,2,3,4,5,6,7,8])
a[::2] = range(10,50,10)
print(a)