from random import randint

secret_num = randint(1, 20)
print("I am thinking of a number between 1 and 20.")
print("Take a guess.")

for guesstaken in range(1, 7):
    guess = int(input(">"))
    if guess < secret_num:
        print("Your guess is too low.")
    elif guess > secret_num:
        print("Your guess is too high.")
    else:
        break


if guess == secret_num:
    print("Good job! You guessed my number in " + str(guesstaken) + " attempts.")

else:
    print(
        "Your attempts are over! The secret number was "
        + str(secret_num)
        + " Start Again"
    )
