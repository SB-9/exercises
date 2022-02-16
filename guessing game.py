# Guessing game made by Samuel Burgess on 17'th Feb 2022

import random

number = random.randint(1, 101)
guess = -111
guesses = 0

GUESS_LIMIT = int(input())
while guess != number and guesses != GUESS_LIMIT:
    guesses += 1
    guess = int(input("Guess the number: "))
    if guess == number:
        print(f"You got it in {guesses} guesses!")
    else:
        if guess < number:
            print("too low")
        else:
            print("too high")
print("you lost")

