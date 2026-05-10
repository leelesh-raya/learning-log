# Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)


import numpy as np

a = np.random.random((10, 2))
print(a)

X, Y = a[:, 0], a[:, 1]

# r = np.sqrt(X**2+Y**2)
r = np.hypot(X, Y)

theta = np.arctan2(Y, X)

b = np.column_stack((r, theta))
print(b)

x = r * np.cos(theta)
y = r * np.sin(theta)

c = np.column_stack((x, y))

print(np.allclose(a, c))
