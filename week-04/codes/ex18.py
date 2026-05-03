# Question: Print or show only 3 decimal places of the numpy array rand_arr.

# Input: rand_arr = np.random.random((5,3)

import numpy as np
arr = np.random.random((5,3))
with np.printoptions(formatter={'float_kind': lambda x:f'{x:.3f}'}):
    print(arr)
rounded=np.round(arr, 3)

print(rounded)