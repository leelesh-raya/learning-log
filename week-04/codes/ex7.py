# Question: Stack the arrays a and b horizontally.

# Input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)
# Output: array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#                [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])


# Solution:
import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

c=np.hstack([a,b])
print(c)
