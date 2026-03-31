'''Problem 3 — List + Logic
Write a function that takes an unsorted list of numbers and returns the list sorted in ascending order. You cannot use .sort(), sorted(), or any built-in sorting function. Implement bubble sort manually.
pythonbubbleSort([64, 34, 25, 12, 22, 11, 90])
# [11, 12, 22, 25, 34, 64, 90]
'''

spam=[1, 2, 3, 4, 5]


def sorter(eggs):
    step=0
    for i in range(len(eggs)-1):
        swapped=False
        for j in range(len(eggs)-1):
            
            if eggs[j]>eggs[j+1]:
                buffer=eggs[j]
                eggs[j]=eggs[j+1]
            
                eggs[j+1]=buffer
            
                swapped=True
            step+=1
        if not swapped:
            break
            
    return eggs, step

print(sorter(spam))




# Correction: Added 'swapped' variable to exit early when no swaps occur, avoiding unnecessary iterations.