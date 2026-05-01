'''Problem 9:
Create two arrays:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
Join them using np.concatenate() in three different ways:

Join vertically (as 2 rows)
Join horizontally (as 2 columns) → you may need to reshape first
Join them into a single 1D array'''

import numpy as np
a=np.array([1, 2, 3])
b=np.array([4, 5, 6])


a1=np.concatenate((a,b), axis=1 )
print(a1)

