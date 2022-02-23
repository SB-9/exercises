def reverse(code):
    password_length = len(password)
    sliced_password = password[password_length::-1]
    return sliced_password


password = input()
answer = reverse(password)
print(answer)
