'''
Given the array:
arr = np.array([10, 25, 56, 89, 34, 67, 12, 45])
Extract the following:

First 4 elements
Last 3 elements
Elements from index 2 to 6 (inclusive)'''

import numpy as np
arr = np.array([10, 25, 56, 89, 34, 67, 12, 45])
print(arr[:4])
print(arr[-3:])
print(arr[2:7])