# price category checker created by Samuel Burgess on 14'th February 2022
age = int(input("please input age: "))

TEENAGER_AGE = 13
ADULT_AGE = 18

if age >= ADULT_AGE:
    print("Adult price")
elif age >= TEENAGER_AGE:
    print("Teenager price")
else:
    print("Child price")
