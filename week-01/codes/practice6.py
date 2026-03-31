# Reverse a list
# Write a function that reverses a list without using .reverse() or [::-1].

import copy

def reverse(lst):
    for i in range(len(lst)//2):
        lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]


spam = [1, 2, 3, 4, 5]
reverse(spam)
print(spam)
