spam=['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
import pprint

def sorter(eggs):
    sortedd={}
    for item in eggs:
        sortedd.setdefault(''.join(sorted(item)), [])
        sortedd[''.join(sorted(item))].append(item)
    return sortedd

pprint.pprint(sorter(spam))

#correction: Used join method for the first time.