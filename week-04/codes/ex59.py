# Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)


import numpy as np

arr = np.random.random((100,2))

x,y = arr[:,0],arr[:,1]
x_dif = np.subtract.outer(x,x)
y_dif = np.subtract.outer(y,y)

D = np.sqrt(x_dif**2 + y_dif**2)

with np.printoptions(threshold=10000):
    print(D)

# Using broadcasting
X,Y = np.atleast_2d(x,y)
D1 = np.sqrt((X-X.T)**2+(Y-Y.T)**2)

# Using scipy
import scipy.spatial
D2 = scipy.spatial.distance.cdist(arr,arr)


print(np.allclose(D,D1))
print(np.allclose(D,D2))