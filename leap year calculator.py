# leap year calculator made by Samuel Burgess
year = int(input("what year is it: "))
if year % 400 == 0:
    print("leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")
