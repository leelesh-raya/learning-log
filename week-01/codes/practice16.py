# Invert a dictionary with duplicate values
# Write a function that swaps keys and values in a dictionary. But handle the case where multiple keys have the same value — in that case the inverted key should map to a list of original keys.
spam={'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
import pprint

def inverter(eggs):
    cheese={}
    for k, v in eggs.items():
        cheese.setdefault(v, [])
        cheese[v].append(k)
    return cheese

pprint.pprint(inverter(spam))


#corrections: None.