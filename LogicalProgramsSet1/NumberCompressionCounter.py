number=int(input("Enter a number: "))
count=0
while number%2==0 and number!=0:
    count=count+1
    number=number//2
print("Count is: ",count)