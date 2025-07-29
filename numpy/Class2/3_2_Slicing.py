import numpy as np


m1 = np.arange(1,10).reshape(3,3)

#slicing #helps to get subpart of the arrays
print('gives only rows filter from m1[:2] ',m1[:2])
print('slicing m1[0:2, 0:2]', m1[0:2, 0:2])

#slicing with rows and columns
print('slicing with rows and columns m1[0:2, 0:2]', m1[0:2, 0:2])   
print('slicing gives all rows and columns m1[:,:]', m1[:,:])

m2 = np.arange(1,13).reshape(3,4)
print('slicking for 1,1 to 2,2 is ', m2[1:3, 1:3])

print('slicing for specific columns only is ', m2[:,1::2])

#question
a = [1,2,3,4,5]
b = [8,7,6] # for b = [3, 0,8,7,6] 3 value also in the final result
a[3:] = b[::-2] #assignment has step size 2
print(a)