import numpy as np
import timeit

a = [1,2,3,4,5 ]
print(type(a))

print(a)

res = [i**2 for i in a]
print(res)

a = np.array([1,2,3,4])

print(a**2)

#performance comaprison
l = range(1000000)
t1 = timeit.timeit('[i**2 for i in l]', globals=globals(), number=1)
print(t1)

l_np = np.array(range(1000000))
t2 = timeit.timeit('l_np**2',globals=globals(), number=1)
print(t2)


#nmpy array
arr1 = np.array(range(10))
print(arr1)

print(arr1.ndim)
print(arr1.shape)# as output is tuple (rows, columns) we get (10,)

#2D array
arr2 = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(arr2)
print(arr2.ndim)
print(arr2.shape)

#number sequences
# print(np.array(range(1,10,0.5))) # start, stop, step(has to be int)

print(np.arange(1,10,0.5)) # start, stop, step(has to be int)

print(np.array([1,2,3.5]))

arrs = np.array([1,2,'satish'])
print(arrs)

#manually speicigy data type while creating the array
arrs = np.array([1,2,4.8], dtype='int')
print(arrs)

print(np.array([1,2,3], dtype='str'))

#homework
# print(np.array([1,2,'4','5.5'], dtype='int'))

#type change after intialization
print(np.array([10,20,30]).astype('float'))

# accessing numpy array elements using #indexing and #slicing
m1 = np.arange(12)
print(m1, m1[0], m1[5], m1[-1]) #m[20] index i is out of bounds

#advanced indexing
m2 = np.array([100,200,300, 400, 500,600])
print('initial m2:', m2)
print(m2[[1,2,1,3,4,2,2]]) #multiple elements with repetition of indices in list form
m2 = np.array([10,100,200,300,400,500,600])
print('m2 after reassignment:', m2)
print('slicing after m2[1:4] is ', m2[1:4])  # slicing
m2[4:]=10
print('after assinging m2[4:]=10 is ',m2)

#2D array
a = np.array(range(10))
a.reshape(2,5)  # reshape the array to 2 rows and 5 columns (gives a new memory)
print(a)