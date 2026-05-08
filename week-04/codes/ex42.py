# Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)

import numpy as np

Z = np.random.uniform(0,10,10)
print(Z-Z%1)
print(Z//1)
print(np.floor(Z))
print(np.trunc(Z))
print(Z.astype(int))