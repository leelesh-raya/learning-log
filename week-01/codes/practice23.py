'''String Manipulation
Write a function that takes a string and 
returns it with every word reversed but the word order kept the same.'''

spam="hello world foo bar"



def rever(eggs):
    lst=[]
    for item in eggs.split():
        buffer=''
        for i in range(-1, -(len(item)+1), -1):
            buffer+=item[i]
        lst.append(buffer)
    return ' '.join(lst)

print(rever(spam))

#Corrections: Used split method with for loop statement and join with return, which made program even simpler.


