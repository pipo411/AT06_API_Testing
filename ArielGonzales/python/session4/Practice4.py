import re

#Verify The format of the username
def usernameRegex():
    username = input("Insert the Username: ")
    regex_username = re.compile("[a-z0-9]+")
    if regex_username.fullmatch(username):
        return "Valid Username"
    else:
        return "Invalid Username"

#Verify The format of the password
def passwordRegex():
    password = input("Insert the Password: ")
    regex_password = re.compile("[a-zA-Z0-9]{8,16}")
    if regex_password.fullmatch(password):
        return "Valid Password"
    else:
        return "Invalid Password"

#Verify The format of the email
def emailRegex():
    email = input("Insert the Email: ")
    regex_email = re.compile("^[a-zA-Z]+(\w+\.?\w+)*\@\w+\.{1}\w{2,3}(\.{1}\w{2})*")
    if regex_email.fullmatch(email):
        return "Valid Email"
    else:
        return "Invalid Email"


print(usernameRegex())
print(passwordRegex())
print(emailRegex())
