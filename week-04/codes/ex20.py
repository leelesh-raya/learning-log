# Question: Limit the number of items printed in python numpy array a to a maximum of 6 elements.


import numpy as np

arr = np.arange(15)

with np.printoptions(threshold=8, edgeitems=4):
    print(arr)