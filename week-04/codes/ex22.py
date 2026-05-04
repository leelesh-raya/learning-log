#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)


import numpy as np

arr = np.array([1,2,0,0,4,0])
nz = np.nonzero(arr)
print(np.where(arr!=0))
print(nz)
