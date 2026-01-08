print("Connected! Welocome to the user for checking Simple intrest")
try:
    p=int(int(input("Enter a value: ")))
    t=int(input("enter time: "))
    r=2
except:
    print("Enter acuerate value")
else:
    res=(p*t*r)/100
    print("Simple Intrest:",res)
print("Connection Terminated")
exit()