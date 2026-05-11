# Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)

import numpy as np

arr = np.zeros(
    (10),
    dtype=[
        ("position", [("x", float, 1), ("y", float, 1)]),
        ("color", [("r", float, 1), ("g", float, 1), ("b", float, 1)]),
    ],
)

arr['color']['r']=32
print(arr[0]['position'])
print(arr)