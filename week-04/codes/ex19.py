# Question: Print or show only 3 decimal places of the numpy array rand_arr.

# Input: rand_arr = np.random.random((5,3))

import numpy as np

rng = np.random.default_rng(42)
arr = rng.random((3,3))/1e3
print(arr)
with np.printoptions(suppress=True, formatter={'float_kind':'{:.6f}'.format}):
    print(arr)

# The suppress parameter in print options is used to control whether scientific notation is used when printing numbers.