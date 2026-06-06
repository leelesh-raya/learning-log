# Learn to implement the model f_{w,b} for linear regression with one variable

import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1, 2])
y_train = np.array([300, 500])

m = x_train.shape[0]
print(m)

i = 1
x_i = x_train[i]
y_i = y_train[i]
print(x_i, y_i)

plt.scatter(x_train, y_train, marker = 'x', c= 'r' )