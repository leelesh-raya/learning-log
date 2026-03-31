'''List Analysis
Write a function that takes a list of numbers and returns a dictionary with these keys: 'mean', 'max', 'min', 'range'. 
Do not use any built-in functions except len(). Calculate everything manually.'''


num=[4, 7, 2, 9, 1, 5]
def analyst(number):
    big=0
    least=number[0]
    total=0
    
    for item in number:
        if item<least:
            least=item
        if item>big:
            big=item
        total+=item
    mean=round(total /len(number), 2)
    return {'Mean': mean, 'max':big, 'min':least, 'Range':big-least }

print(analyst(num))

#Corrections: Returned a dictionary without variable. Thought range is total items in the list.