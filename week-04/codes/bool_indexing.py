#Basic example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

result = arr[arr > 3]
print(result)
result[0]=45
print(arr)
#Creating masks explicitly
mask = arr%2 == 0
print(mask)
print(arr[mask])

#Modifying using Boolean indexing
arr[arr > 3] = 0
print(arr)

#Combining conditions
print(arr[(arr > 2) & (arr < 6)])
print(arr[(arr < 2) | (arr > 5)])

#Negation (NOT)
print(arr[~(arr > 3)])


#Boolean indexing always returns a 1D array of selected elements