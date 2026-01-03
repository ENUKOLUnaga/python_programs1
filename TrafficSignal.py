time=int(input("Enter time"))
time=time%90
if time==0:
    time=90

if time<=30:
    print("RED")
elif time<=45:
    print("YELLOW")
elif time<=90:
    print("GREEN")