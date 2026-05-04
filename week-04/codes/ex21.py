#### 4. How to find the memory size of any array (★☆☆)

import numpy as np

arr = np.zeros((10,10))
arr_size = arr.size*arr.itemsize
print(arr_size)
print(arr.nbytes)