'''Given the array:
Pythonarr = np.arange(1, 31).reshape(5, 6)
Extract:

All even numbers
All numbers divisible by 3
All numbers greater than 15 and less than 25'''

import numpy as np
arr = np.arange(1,31).reshape(5,6)
arr1=arr[arr%2==0]
print(arr1)
arr2=arr[arr%3==0]
print(arr2)
arr3=arr[(arr>15) & (arr<25)]
print(arr3)