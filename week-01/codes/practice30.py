'''
Problem 5 — Everything
Write a function that takes a list of strings, removes duplicates, sorts them by length (shortest 
first), and for strings of equal length sorts them alphabetically. 
Return the result as a single string joined by ' | '.
pythonprocessStrings(["banana", "apple", "kiwi", "fig", "apple", "mango", "kiwi"])
# "fig | kiwi | apple | banana | mango"

'''
spam=["mango", "apple", "mongo", "abple"]

def organise(eggs):
    cheese=[]
    for item in eggs:
        if item not in cheese:
            cheese.append(item)
    for i in range(len(cheese)-1):
        swapped=False
        for j in range(len(cheese)-1):
            if len(cheese[j])>len(cheese[j+1]):
                buffer=cheese[j]
                cheese[j]=cheese[j+1]
                cheese[j+1]=buffer
                swapped=True
                
            elif len(cheese[j])==len(cheese[j+1]):
                a=[cheese[j], cheese[j+1]]
                a.sort()
                cheese[j]=a[0]
                cheese[j+1]=a[1]
                swapped=True
                
                

        if not swapped:
            break
        
    return ' | '.join(cheese)

        

    

    

print(organise(spam))
        

# Correction: Thought the elif block didn't need the swapped flag, but without it the loop exits early before alphabetical sorting completes.

