#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)


import numpy as np

arr = np.arange(1,26).reshape((5,5))

arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print(arr)