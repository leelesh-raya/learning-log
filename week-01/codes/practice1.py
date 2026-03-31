# Ask the user to enter a number. Print whether it is positive, negative, or zero.

while True:
    print("Type a number to find its sign")
    num = float(input(">"))
    if num == 0:
        print("The number is neutral")
    elif num > 0:
        print("The number is positive")
    else:
        print("The number is negative")


# correction: Used float instead of int to include decimal numbers.
