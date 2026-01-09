import csv

file=open(r'C:\Users\ENKOL\PyCharmMiscProject\data1.csv','r')
ro=csv.reader(file,delimiter=',')
print(ro)
file.close()
#file data printing
file=open(r'C:\Users\ENKOL\PyCharmMiscProject\data1.csv','r')
ro=csv.reader(file,delimiter=',')
ld=list(ro)
print(ld)
file.close()
#prinitng row by row
file=open(r'C:\Users\ENKOL\PyCharmMiscProject\data1.csv','r')
ro=csv.reader(file,delimiter=',')
ld1=list(ro)
for row in ld:
    print(row)
file.close()
#printing last value from every line
file=open(r'C:\Users\ENKOL\PyCharmMiscProject\data1.csv','r')
ro=csv.reader(file,delimiter=',')
ld1=list(ro)
for row in ld:
    print(row[-1])
file.close()
#writing data into file
file=open(r'C:\Users\ENKOL\PyCharmMiscProject\data2.csv','w')
wo=csv.writer(file,delimiter=',')
wo.writerow([1,2,3,4])
file.close()
#writing data into file
file=open(r'C:\Users\ENKOL\PyCharmMiscProject\data3.csv','w')
wo=csv.writer(file,delimiter='*')
list1=([1,2,3,4],[5,6,7,8],['a','b','c','d'])
wo.writerows(list1)
file.close()
