# Generate a generic 2D Gaussian-like array (★★☆)


import numpy as np

X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
sigma, mu = 1.0, 0.0
G = np.exp(-((X - mu) ** 2 + (Y - mu) ** 2) / (2.0 * sigma**2))
print(G)