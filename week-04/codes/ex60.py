# How to convert a float (32 bits) array into an integer (32 bits) array in place?

import numpy as np

arr = np.random.rand(10).astype(float)
z = arr.view(int)
z[:] = arr
print(z)



# view: Points to the same address but changes the data type "label."
# [:]: Forces NumPy to refill existing memory instead of creating a new array.