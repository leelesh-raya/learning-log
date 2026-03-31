def comma(list):
    commacode = ""
    for i in range(len(list) - 1):
        commacode = commacode + list[i] + ", "
    commacode = commacode + "and " + list[-1]

    return commacode


spam = ["apples", "bananas", "tofu", "cats"]
print(comma(spam))

# Correction : No corrections! (Couldnt code without debugging though;)
