import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 1. Join vertically → Result will be 2D array (stacked as rows)
result1 = np.concatenate([a.reshape(1,3), b.reshape(1,3)], axis=0)
print(a.reshape(1,3))
