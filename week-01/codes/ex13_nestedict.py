allGuests = {
    "Alice": {"apples": 5, "pretzels": 12, "cups": 2, "cakes": 1},
    "Bob": {"ham sandwiches": 3, "apples": 2, "cups": 5},
    "Carol": {"cups": 3, "apple pies": 1, "pretzels": 4},
    "David": {"apples": 8, "cakes": 2, "ham sandwiches": 1},
    "Eve": {"pretzels": 6, "apple pies": 3, "apples": 1},
    "Frank": {"cups": 7, "cakes": 4, "ham sandwiches": 2},
    "Grace": {"apples": 3, "pretzels": 8, "apple pies": 2},
    "Heidi": {"ham sandwiches": 5, "cups": 4, "cakes": 1},
    "Ivan": {"apples": 6, "cakes": 3, "pretzels": 2},
    "Judy": {"apple pies": 4, "cups": 6, "ham sandwiches": 3},
}


def totalbrought(supply, item):
    numbrought = 0
    for v in supply.values():
        numbrought += v.get(item, 0)
    return numbrought


print("Number of things being brought:")
print("- Apples        ", str(totalbrought(allGuests, "apples")))
print("- Pretzels      ", str(totalbrought(allGuests, "pretzels")))
print("- Apple pies    ", str(totalbrought(allGuests, "apple pies")))
print("- Ham Sandwiches", str(totalbrought(allGuests, "ham sandwiches")))
print("- Cakes         ", str(totalbrought(allGuests, "cakes")))
