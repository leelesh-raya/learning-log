#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)


import numpy as np

rng = np.random.default_rng(42)
arr = rng.random((10,10))
print(arr.min())
print(arr.max())
print(arr.mean())