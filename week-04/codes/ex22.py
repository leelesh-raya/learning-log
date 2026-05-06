#### Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)


import numpy as np

arr = np.array([1,2,0,0,4,0])


#Two possible ways
print(np.where(arr!=0))

nz = np.nonzero(arr)
print(nz)
