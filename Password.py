# Password script made by Samuel Burgess on 17'th Feb 2022
import sys

password = "frojos"
access = "false"
attempts = 0

while access == "false" or attempts != 3:
    if attempts != 3:
        user_password = input("What is the password: ")
        if password == user_password:
            access = "true"
            print("access granted")
            sys. exit()
        else:
            attempts += 1
    else:
        print("too many attempts")
        sys. exit()



