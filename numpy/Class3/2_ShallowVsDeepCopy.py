import numpy as np

l1 = [1,2,3,4]
l2 = l1
l1[0] = 20

#Shallow copy: l2 is a reference to l1, so changes in l1 will reflect in l2
print('Shallow copy:')
print(l1)
print(l2)
print(id(l1), id(l2)) #both refers to same object in memory

a = np.array([1,2,3,4])
b = a+1
print('b is a Deep copy of a, creating a new memory:')
print(a)
print(b)

c = a
c[0] = 100
print('c is a reference to a, so changes in c will reflect in a:')
print(a)
print(c)

#element wise operations are Deep copy

a = np.array([1,2,3,4])
b = a.reshape(2,2)
a[0] = 100

print(a)
print(b)
print(id(a), id(b)) #a and b are different objects in memory, but referring to same header data
print(np.shares_memory(a, b)) #False, b is a Deep copy of a
print(id(a[0]), id(b[0,0])) #a[0] and b[0,0] are different objects in memory


#verfiy it Shallow or Deep copy
a = np.array([1,2,3,4])
b = a.copy()  # Deep copy
print(np.shares_memory(a, b))  # False, b is a Deep copy of a
print(id(a), id(b))  # Different memory addresses

c = a.view()  # Shallow copy
print(np.shares_memory(a, c))  # True, c is a shallow copy of a
print(id(a), id(c))  # Same memory address for data, but different for the



#array splitting
a = np.arange(1,10)
print('Splits the array into 3 equal parts', np.split(a, 3))  # Splits the array into 3 equal parts

print('Splits the array at indexes 3, 5', np.split(a,(3,5))) #splits the array into unequal parts at specified indices
      

a = np.arange(1,17).reshape(4,4)
print(a)
print('#splits the 2D array with default axis=0 (rows)', np.split(a,2)) 
print('#splits the 2D array with axis=1 (columns)',np.split(a,2,axis=1)) 

print('splits the 2D array using hsplit instead of using axis=1', np.hsplit(a,2))  # splits the 2D array into 2 equal parts along columns
print('splits the 2D array using vsplit instead of using axis=0', np.vsplit(a,2))  # splits the 2D array into 2 equal parts along rows

#slicing => giving you 1 subpart of the array
#splitting => giving multiple sub arrys at same time

#stacking arrays
a = np.arange(5)
b = np.arange(5,10)
print('Stacking arrays vertically(append):', np.vstack((a, b)))  # Stacks arrays vertically (row-wise)
print('Stacking arrays horizontally (extend):', np.hstack((a, b)))  # Stacks arrays horizontally (column-wise)

print('Stacking arrays vertically to 3,5 array', np.vstack((a,a,a)))

print('Stacking arrays horizontally to 3 times of array length', np.hstack((a,a,a)))

a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
print('hstack ',np.hstack((a,b)))