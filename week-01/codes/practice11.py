#Move all zeros to the end
#Write a function that moves all zeros to the end while keeping the order of other items.


def movzero(lst):
    zero=0
    for i in range(len(lst)):
        if lst[i]==0:
            zero+=1
    #zero=lst.count=(0)

    while 0 in lst:
        lst.remove(0)

    for i in range(zero):
        lst.append(0)

    



spam=[0, 1, 0, 3, 12]
movzero(spam)
print(spam)


#Correction: COuld have used the count method. But I didn't cover it in my syllabus until now.
