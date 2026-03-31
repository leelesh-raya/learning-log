grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]
heart = ""
for i in range(len(grid[0])):
    # heart=heart+'\n'
    for j in range(len(grid)):
        # heart=heart+grid[j][i]
        print(grid[j][i], end="")
    print()


# Correction: Learned how to use end keyword in print fn to avoid newline and
# use print() to create newline inside a for loop
