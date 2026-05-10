# Create random vector of size 10 and replace the maximum value by 0 (★★☆)

import numpy as np

arr = np.random.random(10)

print(arr.max())

# replace first occurrence of max
arr[arr.argmax()] = 0
print(arr)

# replace all occurrences of max
arr[arr == arr.max] = 0
