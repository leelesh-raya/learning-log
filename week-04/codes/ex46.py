# Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)


import numpy as np

arr = np.linspace(0, 1, 11, endpoint=False)[1:]
print(arr)


# uneven spacing
arr1 = np.random.random(10)
print(arr1)