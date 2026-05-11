# Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

import numpy as np

arr = np.zeros((10,10), dtype=[('x', float),('y', float)])

a = np.linspace(0,1,10)
b = np.linspace(0,1,10)
arr['x'],arr['y']=np.meshgrid(a,b)

print(arr[1,0])