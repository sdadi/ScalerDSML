import numpy as np

a = np.arange(1,13)
print('number of dimension is ',a.ndim)
print('shape of the array is ', a.shape)

print('length of the array is ', len(a))
print('size of the array is ', a.size)

print('reshaped array is a.reshape(4,3)', a.reshape(4, 3))

# -1 means numpy will automatically calculate the number of rows based on the total number of elements and the specified number of columns
print('reshaped array is a.reshape(-1,6)', a.reshape(-1,6))

#transpose of the array means swapping rows and columns
print('before transpose', a.reshape(3, 4))
print('transpose of the array is a.reshape(3,4).T', a.reshape(3, 4).T)

# help(a.T)
# we can get the help documentation using a.T?
print('we can use a.transpose() also ', a.transpose())