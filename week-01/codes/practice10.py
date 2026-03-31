# Chunk a list
# Write a function that splits a list into chunks of size n.
def chunk(lst, n):
    cheese = []
    for i in range(0, len(lst), n):
        eggs = lst[i : i + n]
        cheese.append(eggs)
    return cheese


spam = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(chunk(spam, n))


# Correction: None!
