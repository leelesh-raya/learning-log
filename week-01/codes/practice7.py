# Find the second largest
# Write a function that returns the second largest number in a list.


def sl_num(eggs):
    cheese = sorted(eggs)
    for i in range(-1, -(len(cheese) + 1), -1):
        if cheese[i] != cheese[i - 1]:
            return cheese[i - 1]


spam = [3, 1, 4, 1, 9, 10, 10, 10, 9, 10, 9, 8, 9, 10, 2]
print(sl_num(spam))


# Correction: Used sorted() instead of sort(). Since sorted() returns a new list without modifying the original, the copy module is no longer needed.
