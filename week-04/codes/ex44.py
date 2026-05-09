# Create a 5x5 matrix with column values ranging from 0 to 4 (★★☆)

import numpy as np

# Using reshape and repeat
arr = np.arange(5).reshape(5,1).repeat(5, axis=1)
print(arr)

# Broadcasting
arr = np.zeros((5,5))
arr += np.arange(5).reshape(5,1)
print(arr.astype(int))

# Tile
arr = np.tile(np.arange(5).reshape(5,1), 5)
print(arr)