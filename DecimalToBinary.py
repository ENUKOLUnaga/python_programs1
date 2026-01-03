binary=input("Enter a binary number").strip()
decimal=0
power=0

for i in reversed(binary):
    decimal+=int(i)*(2**power)
    power=power+1
print(decimal)