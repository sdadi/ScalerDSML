import numpy as np

#Q replacing boundary elements with 0
x = np.ones((5,5))
print(x)
y = x[1:-1,1:-1] = 0
print(y)
print(x)


#Q sort birds based on age sort order
birds = np.array(['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills'])
age = np.array([5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0])
sorted_age_index = np.argsort(age)
print('sorted age: ',np.sort(age))
print(sorted_age_index)
print(birds[sorted_age_index])


#Q stack 0 in all 4 sides of matrix
mat = np.array([[1,2],[3,4],[5,6]], dtype=int)
r,c = mat.shape
# print(np.zeros((1,c+2),dtype=int))
print(np.zeros((r,1),dtype=int))  # horizontal stack
result = np.hstack([np.zeros((r,1),dtype=int), mat, np.zeros((r,1),dtype=int)])
print(result)  # horizontal stack
r,c = result.shape
result = np.vstack([np.zeros((1,c),dtype=int), result, np.zeros((1,c),dtype=int)])
print(result)  # vertical stack

#Q split array column wise
arr = np.array([[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11],
 [12, 13, 14, 15],
 [16, 17, 18, 19],
 [20, 21, 22, 23]])

print('subarrays split at cols 0,2,3',np.split(arr,(2,3),axis=1))

#Q split 1D array into equal splits
arr = np.array([0,1,2,3,4,5,6,7,8])
k = 3
print('split array into k equal part:',np.split(arr,k))


#Q output test
arr = np.arange(16).reshape(4,4)
print('split outside boundary: ',np.split(arr,4))

#Q deep copy of array
arr = np.array([1,2,3,0,-2,4])
print(arr*1)
print(arr[:])
print(arr[arr>0])
print(arr.reshape(2,3))