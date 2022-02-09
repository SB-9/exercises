first_name =input("Your first name: ")
last_name =input("Your last name: ")
height =float(input("Your height in meters: "))
age =int(input("Your age: "))
gender =input("he or she: ")
if gender == "he":
    gender_ = "his"
else:  gender_ = "her"
fav_food =input("fav food: ")
print(first_name,last_name)
print(gender_,"height is",height,"m")
print(gender,"is",age,"years old")
print(gender,"likes to eat",fav_food)
print("in 5 years",gender,"will be",age + 5,"years old.")

