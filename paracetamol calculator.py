# Paracetamol calculator script made by Samuel Burgess on 15'th Feb 2022
age = int(input("What is your age: "))
if age < 12:
    weight = int(input("What is your weight: "))
    dose = weight * 10
else:
    dose = 1000
print(f"recomend {dose} paracetamol")
