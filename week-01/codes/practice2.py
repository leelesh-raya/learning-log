# Write a program that prints the multiplication table of any number the user enters. From 1 to 10.

num = int(input("Enter a number:"))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# correction: Used f-strings
