password = input()
password_length = len(password)
sliced_password = password[password_length::-1]
print(sliced_password)
