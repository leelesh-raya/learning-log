'''
Problem 4 — Nested Dictionary
Write a function that takes a list of transaction dictionaries and returns a summary dictionary 
with each person's total spent, average transaction, and number of transactions.
'''




spam= [
    {'name': 'Alice', 'amount': 50},
    {'name': 'Bob', 'amount': 30},
    {'name': 'Alice', 'amount': 70},
    {'name': 'Bob', 'amount': 20},
    {'name': 'Alice', 'amount': 30}
]
    


def transum(eggs):
    cheese={}

    for item in eggs:
        
            cheese.setdefault(item['name'], {'total':0, 'avg':0, 'count': 0})
            cheese[item['name']]['total']+=item['amount']
            cheese[item['name']]['count']+=1
            cheese[item['name']]['avg']=round(cheese[item['name']]['total']/cheese[item['name']]['count'], 2)

        
            
            


        
    return cheese

print(transum(spam))


# Correction: Initialized with zeros using setdefault, allowing the same update logic to run
# for every transaction, eliminating the need for if/else blocks.
