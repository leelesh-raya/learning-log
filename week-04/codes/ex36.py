# How to round away from zero a float array ? (★☆☆)

import numpy as np

arr = np.random.uniform(-10,+10,10)
print(arr)


print(np.copysign(np.ceil(np.abs(arr)), arr))

# More Readable but less efficient. Because it computes both np.ceil(Z) and np.floor(Z) for the entire array before selecting
print(np.where(arr>0, np.ceil(arr), np.floor(arr)))