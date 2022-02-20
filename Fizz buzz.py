# fizz buzz script made by Samuel Burgess on 16'th feb 2022

user_number = int(input())

for number in range(1, (user_number + 1)):
    if number % 15 == 0:
        print("Fizzbuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
