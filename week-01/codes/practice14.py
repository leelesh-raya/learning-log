#You have a list of words. Write a function that returns a dictionary where each letter of the alp


spam=['apple', 'banana', 'avocado', 'blueberry', 'cherry', 'apricot']

def organise(eggs):
    bucket={}
    for item in eggs:        
        bucket.setdefault(item[0], [])
        bucket[item[0]].append(item)
    return bucket

backpack=organise(spam)
print(backpack)

        

    

# Correction: Didn't think I could use a slice as a parameter for the setdefault method.