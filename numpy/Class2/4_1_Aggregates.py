import numpy as np

#aggregates
#sum, avg, min, max

m1 = np.arange(1,13).reshape(3,4)
print(m1)
print('sum of all elements: is ',np.sum(m1))
print('min value is ',np.min(m1))
print('max value is ',np.max(m1))
print('average value is ',np.mean(m1), np.average(m1))#for average

print('lowest value per row/horizontally is ',np.min(m1, axis=1))
print('lowest value by row/vertically is ', np.min(m1, axis=0))

print('avg value per row/horizontally is ', np.mean(m1, axis=1))
print('avg value by row/vertically is ', np.mean(m1, axis=0))

m2 = m1[:,[0,1]]
print('mean of first two columns is ', np.mean(m2, axis=0), np.average(m2, axis=0))

