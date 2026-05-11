# How to print all the values of an array? (★★☆)

import numpy as np

arr = np.zeros((40, 40))

print(arr)

with np.printoptions(threshold=float("inf")):
    print(arr)

# inf doesnot exist for int type
