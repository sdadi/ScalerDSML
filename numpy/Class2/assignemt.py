import numpy as np

#1 condition check
arr = 2 * np.arange(0,2,0.5)
if arr <= 0.6:
    print("condition satisfies")
else:
    print("condition doesn't satisfy")
    
#2 filter based on mask
a = np.array([85, 18, 2, 57, 65, 44])
mask = a > 40
print(a[mask])

a = np.array([[1,1],[1,1]])
print(a*np.array([[2,2]]))