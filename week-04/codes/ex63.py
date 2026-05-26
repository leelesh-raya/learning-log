# Generate a generic 2D Gaussian-like array (★★☆)


import numpy as np

X, Y = np.meshgrid(np.linspace(-1, 1, 4), np.linspace(-1, 1, 4))
sigma, mu = 1.0, 0.0
G = np.exp(-((X - mu) ** 2 + (Y - mu) ** 2) / (2.0 * sigma**2))
print(G)

# Output is a 2D array because meshgrid takes two 2D arrays and turns them into two 2D arrays(X,Y)


x = np.linspace(-1,1,4)
y = np.linspace(-1,1,4)
sigma , mu = 1.0 , 0.0
x = x[:, None]
y = y[None, :]
gx = np.exp(-((X - mu) ** 2) / (2.0 * sigma**2))
gy = np.exp(-((Y - mu) ** 2) / (2.0 * sigma**2))
O = gx*gy
print( O)