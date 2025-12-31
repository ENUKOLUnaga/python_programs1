#Printing first 10 numbers
number=1
while number<=10:
    print(number)
    number=number+1

#Break usage
number2=1
while number2<=10:
    print(number2)
    if number2==5:
        break
    number2=number2+1
#Continue usage
number3=0
while number3<10:
    number3=number3+1
    if number3==5:
        continue
    print(number3)
else:
    print("Goodbye")
#For Loop Example
for x in "Python":
    print(x)
#Break usage in for loop
fruits=["Apple","Orange","Pineapple"]
for x in fruits:
    print(x)
    if x=="Orange":
        break
#Continue usage in for loop
for x in fruits:
    if x=="Orange":
        continue
    print(x)

#Range function
for x in range(10):
    print(x)
for x in range(2,10):
    print(x)
for x in range(2,10,3):
    print(x)
#else usage
for x in range(10):
    print(x)
else:
    print("number printing finshed")

#nested loops usage
adj=["red","green","blue"]
fruit=["Apple","Orange","Pineapple"]
for x in adj:
    for y in fruit:
        print(x,y)

#python Arrays..
cars=["volvo","benz","tata"]
for x in cars:
    print(x)
#update and adding into arrays
cars[1]="suzuki"
for x in cars:
    print(x)
cars.append("Mercedes")

for x in cars:
    print(x)
#Pop() and remove()
cars.pop(2)
cars.remove("suzuki")
for x in cars:
    print(x)
print(cars.count("suzuki"))#count()
