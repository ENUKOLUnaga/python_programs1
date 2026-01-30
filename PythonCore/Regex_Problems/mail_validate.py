import re
text='''
ramu@gmail.com,
ramu@@gmail.com
ramu<>@gmail.com
ram-dev@gmail.com
ram@yahoo.com
'''
#pattern=r"[a-zA-Z0-9_\-$]+@[a-zA-Z]+.com"
#match=re.findall(pattern,text)
#print(match)
pattern=r"([a-zA-Z0-9_$\-]+)@([a-zA-Z]+.com)"
itr=re.finditer(pattern,text)
for l in itr:
    print(l.group(0))
    print(l.group(1))
    print(l.group(2))
pattern1=r"[a-zA-Z]+.com"
s=re.sub(pattern1,"@self.com",text)
s1=re.subn(pattern1,"@self.com",text)
print(s)
print(s1)