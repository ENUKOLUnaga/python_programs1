#List implementation
lst1=[1,"Hello",3.5,True]
print(lst1)
print(type(lst1))
print(lst1[0])
print(lst1[-4])
lst1.append("Hell")
print(lst1)
lst1.remove("Hell")
print(lst1)
print(lst1[::])
print(lst1[::-1])
print(lst1[1:3])
print(lst1[-2:-4:-1])
lst1[::2]=[99,99]
print(lst1)
print(lst1.count(99))
#List Comprehension
lst=[2,4,5,6,7]
sq_lst=[i**2 for i in lst if i%2==0]
print(lst,sq_lst)

s="Knowledge is matter"
lst3=s.split()
print(lst3)
lst4=[]
for c in range(len(lst3)):
    if c>len(lst3):
        lst4.append(lst3[c].upper())
    else:
        lst4.append(lst3[c].lower())
print(' '.join(lst4))
#Set Comprehension
s1={1,2,3,4,5,6,7,8,9}
res={i**2 for i in s1 if i%2==0}
print(res)
re2={i**2 if i%2==0 else i+i for i in s1}
print(re2)

#Dictionaries
d={1:"java",
   2:"python",
   3:"c++",
   4:"c"}
print(d.keys())
d1=input()
s2={}
for i in d1:
    if i not in s2:
        s2[i]=1
    else:
        s2[i]=s2[i]+1
print(s2)