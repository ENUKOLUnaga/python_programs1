from re import Match

number1=int(input("enter first number"))
number2=int(input("enter second number"))
if number1>number2:
    print("number1 is greater than number2")

#multiple statements inside if block
age=int(input("enter age"))
if age>=18:
    print("age is greater than 18")
    print("You can vote")
    print("You have legal rights")

#using variables to check condition
is_logged=True
if is_logged:
    print("logged in")

#Elif condition
print("Elif checking")
if number1>number2:
    print("number1 is greater than number2")
elif number1==number2:
    print("number1 is equal to number2")
#Multiple Elif conditions
score = int(input("enter score"))
if score>=90:
    print("Grade : A")
elif score>=80:
    print("Grade : B")
elif score>=70:
    print("Grade : C")
elif score>=60:
    print("Grade : D")

#Week Checker
Day =int(input("enter day"))
if Day ==1:
    print("Sunday")
elif Day ==2:
    print("Monday")
elif Day ==3:
    print("Tuesday")
elif Day ==4:
    print("Wednesday")
elif Day ==5:
    print("Thursday")
elif Day ==6:
    print("Friday")
elif Day ==7:
    print("Saturday")
#Else condition
if number1>number2:
    print("number1 is greater than number2")
elif number1==number2:
    print("number1 is equal to number2")
else:
    print("number1 is less than number2")

#Score checker by using else
if score>=90:
    print("Grade : A")
elif score>=80:
    print("Grade : B")
elif score>=70:
    print("Grade : C")
elif score>=60:
    print("Grade : D")
else:
    print("Grade : E")

email=input("enter email")
if len(email)>0:
    print(f"Welcome!{email}")
else:
    print("please enter your Correct email")
#Short Hand if
print("number1 is greater than number2") if number1>number2 else print("number1 is less than number2")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

#pass statement
if score>=90:
  pass
print("score is passed")

#Match statement
match Day:
    case 1:print("Sunday")
    case 2:print("Monday")
    case 3:print("Tuesday")
    case 4:print("Wednesday")
    case 5:print("Thursday")
    case 6:print("Friday")
    case 7:print("Saturday")
    case _:print("Invalid input")
