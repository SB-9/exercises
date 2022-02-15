# grade calculator created by Samuel Burgess on 14'th February 2022
mark = int(input("Enter mark: "))
A = 90
B = 70
C = 50

if mark >= A:
    print(f"{mark} is grade A")
elif mark >= B:
    print(f"{mark} is grade B")
elif mark >= C:
    print(f"{mark} is grade C")
else:
    print(f"{mark} is a fail")
