# What are the result of the following expressions? (★☆☆)

import numpy as np

print(np.array(0) / np.array(0)) # Dividing anything by zero is undefined in mathematics.
# nan

print(np.array(0) // np.array(0)) # Floor division returns integers. But 'nan' concept exists only for floats
# 0
# the NumPy source code for integer floor division simply returns 0 for the divide-by-zero case as a hardcoded fallback.

print(np.array([np.nan]).astype(int).astype(float))
# [-9.22337204e+18]
# nan has no integer representation — astype(int) silently replaces it with minimum int64 value
# converting back to float gives a large negative number, original nan is lost permanently



# Lesson: Always check for nan before converting types