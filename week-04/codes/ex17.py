# Question: Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.


import numpy as np
rng = np.random.default_rng(42)
arr = rng.uniform(5, 10, (5,3))
print(arr)