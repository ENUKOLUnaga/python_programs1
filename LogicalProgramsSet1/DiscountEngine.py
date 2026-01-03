amount=float(input("Enter a number"))
if amount>=5000:
    amount=amount-(amount*0.20)
elif amount>=3000:
    amount=amount-(amount*0.10)
elif amount>=1000:
    amount=amount-(amount*0.05)
else:
    amount=amount
print(amount)