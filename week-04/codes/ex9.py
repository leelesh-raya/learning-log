# Question: Get the common items between a and b

# Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#        b = np.array([7,2,10,2,7,4,9,4,9,8])

# Output: array([2, 4])


# Solution:
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b)
d=np.unique(a[np.isin(a,b)])
#e=np.unique(np.isin(a,b))
print(c)
print(d)
#print(e) return [false true]