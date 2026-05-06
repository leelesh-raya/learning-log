#  What is the output of the following script? (★☆☆)


print(sum(range(5), -1)) #prints 9 because python's built sum() function is used

from numpy import *  #It imports everything from NumPy directly into namespace
print(sum(range(5), -1)) # Prints 10. Second argument is axis. 

# axis=-1 means last axis
# range(5) is 1D — last axis is axis 0
# sums everything = 10