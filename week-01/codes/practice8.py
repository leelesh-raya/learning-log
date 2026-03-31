# Flatten a nested list
# Write a function that flattens a list of lists into a single list.


def single(lst):
    new = []
    for i in lst:
        if type(i) == list:
            for j in i:
                new.append(j)
        else:
            new.append(i)
    return new


spam = [[1, 2], [3, 4], [5, 6], 7, 8]
print(single(spam))


# Correction: None!
