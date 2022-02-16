# Password script made by Samuel Burgess on 17'th Feb 2022


password = "frojos"
access = "false"

while access == "false":
    user_password = input("What is the password: ")
    if password == user_password:
        access = "true"
        print("access granted")



