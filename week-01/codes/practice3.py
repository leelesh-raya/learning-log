# Ask the user to keep entering numbers until they type done. At the end print the total sum of all numbers entered.

total = 0
while True:
    num = input('Enter a number (or "done" to finish): ')
    if num == "done":
        break
    total = total + float(num)
print(total)


# Correction: Understood how to code when the input is either a string or number.
