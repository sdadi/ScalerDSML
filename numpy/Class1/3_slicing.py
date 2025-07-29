import numpy as np

s1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print('slicking of s1[5::1] is : ', s1[5::1])  # Output: [ 6  7  8  9 10]
print('slicking of s1[5::2] is : ', s1[5::2])  # Output: [ 6  8 10]
print('slicing of s1[-5:-1] is : ', s1[-5:-1])  # Output: [6 7 8 9]
print('slicking of s1[-5:1:-1] is: ', s1[-5:1:-1])  # Output: [6 5 4 3 2]
print('slicking of s1[-5:1:1] is: ', s1[-5:1:1])  # Output: [6 5 4 3 2]
print('slicking of s1[-5:-1:-1] is: ', s1[-5:1:-1])  # Output: [6 5 4 3 2]