import re
def valid_password(stri):
    pwd_check = re.compile(r'''((?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%]).{8,16})''')
    return pwd_check.findall(stri)

pwd = input("Please enter your password")

if len(valid_password(pwd)) == 0:
    print("Password is not strong")
else:
    print("Password is Valid")
