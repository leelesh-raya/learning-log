# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)

import numpy as np

a = np.arange(1, 16).reshape(5, 3)
b = np.arange(20, 26).reshape(3, 2)

print(a @ b)
#print(np.matmul(a,b))