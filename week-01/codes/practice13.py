#Running total
#Write a function that takes a list of numbers and returns a new list where each item is the sum of all previous items including itself.

def runtot(eggs):
    cheese=[]   
    total=0
    for item in eggs:
        total+=item
        cheese.append(total)
    return cheese

spam=[1, 2, 3, 4, 7]
runtot(spam)
print(runtot(spam))