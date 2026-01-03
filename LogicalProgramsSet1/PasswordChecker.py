password=input("Enter your password: ")
digit=False
upper=False
for ch in password:
    if ch.isdigit():
        digit=True
    elif ch.isupper():
        upper=True
if len(password)>=8 and digit and upper:
    print("Strong")
else:
    print("Weak")