# . Remove duplicates
# Write a function that removes duplicate items from a list while keeping the original order.
import copy


def dedupl(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen


spam = [1, 2, 2, 3, 1, 4, 5, 6, 7, 9, 9, 8, 8, 7, 3, 10, 44, 2, 44]
spam = dedupl(spam)
print(spam)

# Correction: Didn't know i could use the "not in" operator. It simplified my program.
