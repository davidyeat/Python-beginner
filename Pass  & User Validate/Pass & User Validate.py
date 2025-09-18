import re
def username_validate(username):
    if len(username) > 15:
        print("Your username can't be longer than 12 characters.")
        return False
    elif not username.find(' ') == -1:
        print("Your username can't contain whitespace.")
        return False
    elif not username.isalpha():
        print("Your username can't contain numbers.")
        return False
    else:
        return True
def password_validate(password):
    if len(password) < 8:
        print("Password must be at least 8 characters.")
        return False
    elif not re.search(r"[!@#$%^&*()-_+={[}\]|\\:;\"'<>,.?/~`]", password):
        print("Password must contain at least one special characters.")
        return False
    elif re.search(r"\s", password):
        print("Password cannot contain whitespace.")
        return False
    elif not re.search(r"\d", password):
        print("Your password must contain at least one digit.")
        return False
    elif not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    elif not re.search(r"[a-z]", password):
        print("Password must contain at least one lower case letter.")
        return False
    else:
        return True
print("*** Welcome to Sign Up system ***")
Username = input("Enter your username: ")
Password = input("Enter your password: ")
if username_validate(Username) and password_validate(Password):
    print("Username and Password Valid!")
else:
    print("Username or Password failed.")

