import pprint

inv = {"gold coin": 42, "rope": 1}
dragonLoot = [
    "gold coin",
    "dagger",
    "gold coin",
    "gold coin",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "ruby",
    "egg",
]


def add2inventory(bag, loot):
    counts = {}
    for item in loot:
        counts.setdefault(item, 0)
        counts[item] += 1

    for item, total in counts.items():
        bag.setdefault(item, 0)
        bag[item] += total


add2inventory(inv, dragonLoot)
pprint.pprint(inv)
