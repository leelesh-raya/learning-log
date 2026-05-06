#Create a 3x4 array filled with zeros. Then change its data type to int32.

import numpy as np

arr = np.zeros((3, 4))
arr = arr.astype("int32")
print(arr.dtype)
print(arr)
