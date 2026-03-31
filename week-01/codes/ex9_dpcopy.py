import copy


def eggs(someParameter):
    someParameter[5].append(999)


spam = ["a", 2, 3, 4, ["a", 2, 3, 4]]

spam.insert(3, "donu")
# china = copy.deepcopy(spam)
# eggs(china)
# print(china)
italy = copy.deepcopy(spam)
eggs(italy)
print(italy)
print(spam)
