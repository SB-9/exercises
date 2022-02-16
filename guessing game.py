# Guessing game made by Samuel Burgess on 17'th Feb 2022

import random

number = random.randint(1, 11)
guess = -111

while guess != number:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You got it")
    else:
        print("wrong!")

