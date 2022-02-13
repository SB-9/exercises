age = float(input("What is your age: "))
temperature = float(input("What is your temperature: "))
if age < 2 and temperature >= 38:
    print("call a doctor")
elif temperature > 39.5:
    print("High fever")
else:
    print("You're fine")
