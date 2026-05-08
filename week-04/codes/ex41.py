# How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)

import numpy as np

A = np.array([1, 1, 1], dtype=np.float64)
B = np.array([2, 2, 2], dtype=np.float64)

np.add(A, B, out=B)
np.divide(A, 2, out=A)
np.negative(A, out=A)
np.multiply(A,B, out=A)
print(A)

# Lesson: All numpy ufuncs support out