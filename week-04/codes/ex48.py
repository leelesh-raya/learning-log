# How to sum a small array faster than np.sum? (★★☆)

import numpy as np

arr = np.arange(10)
print(np.add.reduce(arr))

# np.add.reduce skips np.sum overhead and directly collapses the array 
# worth using when array is small and called repeatedly, 
# since overhead time exceeds computation time in that case