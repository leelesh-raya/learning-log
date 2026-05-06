# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)


import numpy as np

arr = np.diag((np.arange(1,5)), k=-1)
print(arr)