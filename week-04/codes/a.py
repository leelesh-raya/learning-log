import numpy as np

# Consider two random arrays A and B, check if they are equal (★★☆)


import numpy as np

import scipy.spatial

Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)