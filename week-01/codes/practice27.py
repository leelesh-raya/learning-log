'''Problem 2 — String + Dictionary
Write a function that takes a string and returns the first non-repeating character. 
If all characters repeat, return None. Ignore spaces.
pythonfirstUnique("programming is cool")
# 'p'  (first character that appears exactly once)'''

spam="pprograamminng sis ccooll"

def notrep(eggs):
    cheese={}
    for char in ''.join(eggs.split()):
        cheese.setdefault(char, 0)
        cheese[char]+=1

    for char in cheese:
        if cheese[char]==1:
            return char
    
    return

         


print(notrep(spam))


#Correction: None.