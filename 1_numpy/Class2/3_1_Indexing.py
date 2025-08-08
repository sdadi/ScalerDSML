import numpy as np

m1 = np.arange(1,10).reshape(3,3)

print('reshaped array is ', m1)
print('printing a position in 2 ways m1[r,c] and m1[r][c]', m1[0,0], m1[0][0])
print('row 3 and column 1 value is ', m1[2, 0], type(m1[2, 0]))

#passing multiple position indexes
print('multiple position indexes', m1[[0, 1, 2], [0, 1, 2]])
