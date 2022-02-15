# Paracetamol calculator script made by Samuel Burgess on 15'th Feb 2022
age = int(input("What is your age: "))
weight = int(input("What is your weight: "))
if age < 12:
    dose = weight * 10
else:
    dose = 1000
print(f"recomend {dose} paracetamol")
