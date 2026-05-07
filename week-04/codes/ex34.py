# Consider an integer vector Z, which of these expressions are legal? 

import numpy as np

Z = np.array([1, 2, 3, 4])

print(Z**Z) #  Legal. Each element raised to itself
# [  1   4  27 256]

print(2 << Z >> 2) # Legal. Bitwise shift 2 (0010) Z times, then shift the result two times.
# [1 2 4 8]

print(Z <- Z) # Legal but misleading. This is NOT "less than or equal" but is Z less than negative Z?
# [False False False False]

print(1j*Z) # Legal. Multiplies each element with complex number (0+1j)
# [0.+1.j 0.+2.j 0.+3.j 0.+4.j]

print(Z/1/1) # Legal. Division by 1 returns same numbers in dtype float64.
# [1. 2. 3. 4.]

print(Z<Z>Z)