# Blood donor calculator made by Samuel Burgess on 14'th February 2022
age = float(input("What is your age: "))
weight = float(input("What is your weight in Kilograms: "))

AGE_LIMIT = 16
WEIGHT_LIMIT = 50
if age > AGE_LIMIT and weight < WEIGHT_LIMIT:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")
