import csv
"""
file1=open('C:\\Users\\ENKOL\\PyCharmMiscProject\\data4.csv','w')
wo=csv.writer(file1,delimiter=',')
n=int(input("enter number of students: "))
for i in range(n):
    rollnumber=int(input("Enter rollnumber: "))
    name= input("Enter name: ")
    age=int(input("Enter age: "))
    std=int(input("Enter standard: "))
    percentage=float(input("Enter percentage: "))
    wo.writerow([rollnumber,name,age,std,percentage])
file1=open('C:\\Users\\ENKOL\\PyCharmMiscProject\\data4.csv','a')
wo=csv.writer(file1,delimiter=',')
n=int(input("enter a number students: "))
for i in range(n):
    rollnumber=int(input("Enter rollnumber: "))
    name= input("Enter name: ")
    age=int(input("Enter age: "))
    std=int(input("Enter standard: "))
    percentage=float(input("Enter percentage: "))
    wo.writerow([rollnumber,name,age,std,percentage])
file1.close()
"""
file1=open('C:\\Users\\ENKOL\\PyCharmMiscProject\\data4.csv','r')
ro=csv.reader(file1,delimiter=',')
print(ro)
lst=list(ro)
sum_percentage=0
n=0
for i in lst:
    if len(i)>0:
        sum_percentage=sum_percentage+float(i[-1])
        n=n+1
print("overall percentage = ",sum_percentage/n)
file1.close()