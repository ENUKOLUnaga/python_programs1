salary=float(input("Enter your salary: "))
late_days=int(input("Enter late days: "))
absent_days=int(input("Enter absent days: "))
deduction=0
if late_days>10:
    deduction+=0.10
elif late_days>5:
    deduction+=0.05

if absent_days>10:
    deduction+=0.10
salary=salary-(salary*deduction)
print(salary)