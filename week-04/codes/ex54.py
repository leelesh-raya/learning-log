# Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

import numpy as np

x=np.arange(9)
y=x+0.5 # 0.5 is just a clean, arbitrary choice to ensure no division by zero occurs.

C = 1/np.subtract.outer(x,y)

print(np.linalg.det(C))