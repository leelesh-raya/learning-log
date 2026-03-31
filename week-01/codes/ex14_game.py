inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def open(bag):
    print("Bag contains:")
    total = 0

    for k, v in bag.items():
        total += v
        print(v, k)
    print("Total items:", total)


open(inventory)
