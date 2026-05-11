# How to find the closest value (to a given scalar) in a vector? (★★☆)

import numpy as np

a = np.random.randint(0, 100, (100))
b = np.random.uniform(0, 100)
print(b)

index = np.abs(a - b).argmin()
print(a[index])
