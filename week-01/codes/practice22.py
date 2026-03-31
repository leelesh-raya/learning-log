'''Everything Combined
Write a function that takes a string and returns the most frequent character (ignore spaces). 
If there's a tie return all tied characters as a sorted list.'''


spam="programming is hard"

def freq(text):
    store={}
    winner=[]
    lst=text.split()    
    for item in lst:
        for i in range(len(item)):
            store.setdefault(item[i], 0)
            store[item[i]]+=1
    value=0
    for k,v in store.items():
        if v>value:
            winner=[k]
            value=v
        elif v==value:
            winner.append(k)
    if len(winner)==1:
        print("'"+winner[0]+"' (appears",store[winner[0]],"times)")
    else:
        for item in winner:
            print("'"+item+"' (appears",store[item],"times)")

freq(spam)


# correction: assigned 'value' with the count of the first letter in store,
# turns out it missed the first character as a potential winner

       
            


    

