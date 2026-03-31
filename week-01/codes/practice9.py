# Rotate a list
# Write a function that rotates a list by n positions.


def rotate(lst, n):
    return lst[n:]+lst[:n]

spam = [1, 2, 3, 4, 5]
n = 2
print(rotate(spam, n))



# Correction: Used slicing instead of two 'for-loops' whcih made program more simple.
