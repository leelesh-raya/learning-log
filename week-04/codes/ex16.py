# Question: Reverse the rows of a 2D array arr.

# Input:


import numpy as np
arr = np.arange(9).reshape(3,3)

print(arr)

print(arr[::-1,])
print(arr[::-1,::-1])
print(arr[::-1,])