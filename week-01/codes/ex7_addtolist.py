veggies = []
while True:
    print(
        "Enter the name of the vegetable "
        + str(len(veggies))
        + " Or enter nothing to stop"
    )
    name = input(">")
    if name == "":
        break
    veggies = veggies + [name]

print("List of vegetables to buy")
for names in range(len(veggies)):
    print(names, " " + veggies[names])
