import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+\.(com)$'

    if re.match(pattern, email):
        domain = email.split('@')[1]

        if domain in ["gmail.com"]:
            return True

    return False

email = input("Enter email address: ")

if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")