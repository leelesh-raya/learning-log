# Consider an integer vector Z, which of these expressions are legal? 

import numpy as np

Z = np.array([1, 2, 3, 4])

print(Z**Z)
print(2 << Z >> 2)
print(Z <- Z)
print(1j*Z)
print(Z/1/1)
#print(Z<Z>Z)
