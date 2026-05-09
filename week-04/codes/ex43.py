# Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)

import numpy as np

# rehsape and repeat
arr = np.arange(5).reshape(1,5).repeat(5, axis=0)
print(arr)

# Broadcasting
arr = np.zeros((5,5))
arr += np.arange(5)
print(arr)

# tile
arr = np.tile((np.arange(5)), (5,1))
print(arr)


