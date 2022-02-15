DRIVING_AGE = 16
age = int(input("what is your age: "))
if age >= DRIVING_AGE:
    can_drive = "true"
else:
    can_drive = "false"
if can_drive == "true":
    print("User can apply for license")
else:
    print("user cannot apply for license")
