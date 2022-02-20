# fizz buzz script made by Samuel Burgess on 16'th feb 2022

user_number = int(input("How many numbers?: "))

for number in range(1, (user_number + 1)):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)
