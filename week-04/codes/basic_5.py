'''
Create a 2D array of shape (6, 5) with random integers between 10 and 100 (inclusive).
Then do the following:

Extract the first 3 rows
Extract the last 2 columns
Extract the center 2x2 sub-array (rows 2-3, columns 2-3)
Extract all elements that are greater than 50'''

import numpy as np
arr = np.random.randint(10, 101, (6,5))
print(arr)
print(arr[:3])
print(arr[:, -3:])
print(arr[2:4, 2:4])
arr1=arr[arr>50]
print(arr1)