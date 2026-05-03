# Question: Convert the function maxx that works on two scalars, to work on two arrays.
# Input:

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

# maxx(1, 5)
#> 5

# Output:
# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])
# pair_max(a, b)
# array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])

# Solution

import numpy as np

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

def pair_max(x,y):
    #z=list(map(lambda a,b:max(a,b), x,y ))
    #z=[max(m,n) for (m,n) in list(zip(x,y))]
    z=np.maximum(x,y)
    return z

print(pair_max(a,b))