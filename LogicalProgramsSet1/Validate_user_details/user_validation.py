import re
#validate email 
def valid_email(email):
    pattern = r'^[a-z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
#validate password
def valid_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*]).{8,}$'
    if re.match(pattern,password):
        return True
    else:
        return False

def main():
    email=input("Enter a valid email: ")
    password=input("Enter a password: ")
    if valid_email(email) and valid_password(password):
        print("valid user!")
    else:
        print("Invalid User")

if __name__=="__main__":
    main()