# fizz buzz script made by Samuel Burgess on 16'th feb 2022

for number in range(1,101):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)
