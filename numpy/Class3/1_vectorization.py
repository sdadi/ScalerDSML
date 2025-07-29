import numpy as np

a = np.arange(10,20)
print(a)
print(a*2)


import math
print(math.factorial(5)) # only accespts integer scalar value


def new_ops(x):
    if x%2 == 0:
        return x**2
    else :
        return x**3
    
print(new_ops(2))
for i in a:
    print(new_ops(i))# iterative loop is brute force way (non vectorized way)

vec_ops = np.vectorize(new_ops) # uses Python loop under the hood
print(vec_ops(a)) # vectorized way

vec_factorial = np.vectorize(math.factorial)
print(vec_factorial(a)) # vectorized way

a = np.arange(1,6)
print('each element multiplied b 5: ', a*5)

b= np.arange(6,11)
print(a)
print(b)
print('two 1D array muliplication: ',a*b)#both arrays should be same size

#array to array multiplication is different than 2D matrix multiplication
#fromn python3.5 onwards we can use 
# np.matmul(a,b) -> generally preferable for more than 3D arrays
# np.dot(a,b)    -> generally preferable for 1D, 2D, scalar multiplication
# a@b 


m1 = np.arange(1,5).reshape(2,2)
m2 = np.arange(2,8).reshape(2,3)
print(m1)
print(m2)
print('2D matrix multiplication with np.matmul: ', np.matmul(m1, m2)) #supports only array to array matrix multiplication
print('2D matrix multiplication with np.dot: ', np.dot(m1, m2)) # can multiply for array to array or array to scalar
print('2D matrix multiplication with @: ', m1 @ m2) 