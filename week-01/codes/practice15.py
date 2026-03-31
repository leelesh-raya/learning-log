# Write a function that takes a start number, stop number, and divisor as user inputs, and groups all numbers in that range by their remainder when divided by the divisor.
# Print the result as a prettified dictionary.
import pprint


def remainder(s, st, d):
    spam = {}
    for i in range(s, st + 1):
        spam.setdefault((i % d), [])
        spam[(i % d)].append(i)
    pprint.pprint(spam)


print("Type the range of numbers and the divisor")
start = int(input("Start from:"))
stop = int(input("Upto:"))
divisor = int(input("Divisor:"))
remainder(start, stop, divisor)


