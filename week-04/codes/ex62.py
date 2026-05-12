#  What is the equivalent of enumerate for numpy arrays? (★★☆)\

import numpy as np
arr = np.arange(9).reshape(3,3)

for index, value in np.ndenumerate(arr):
    print(index, value)

for index in np.ndindex(arr.shape):
#for index in np.ndindex((3,3)):   
    print(index, arr[index])

# shape is used as the argument because we are not dealing with any values. Indexes for similar shapes are same. 