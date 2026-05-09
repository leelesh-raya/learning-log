# Create a random vector of size 10 and sort it (★★☆)


import numpy as np
arr = np.random.random(10)
arr.sort()
print(arr)


# not in-place — returns new sorted array, Z unchanged
sorted_arr = np.sort(arr)
print(sorted_arr)   # [1, 1, 2, 3, 4, 5, 6, 9]
print(arr)          # [3, 1, 4, 1, 5, 9, 2, 6] — unchanged