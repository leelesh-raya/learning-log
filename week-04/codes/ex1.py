'''Create a 4x4 array using np.arange(16).reshape(4,4).
Then do the following:

Flatten it using flatten()
Flatten it using ravel()

Check which one returns a view and which returns a copy using the .base attribute.'''


import numpy as np
arr=np.arange(16).reshape(4,4)
arr1=arr.flatten()
arr2=arr.ravel()
print(arr1.base)
print(arr2.base)
#flatten() returns copy
#ravel() returns view