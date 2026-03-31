'''List Logic
Write a function that takes two lists and returns a third list 
containing only elements that appear in both lists, without duplicates.'''

x=[1,2,3,4,5,2]
y=[2,3,4,5,6,7,3]
def common(a,b):
    new=[]
    for item in a:
        if item in b and item not in new:
            new.append(item)
                   
    return new
print(common(x, y))



#Corrections: Used 'and' operator to avoid duplicates.