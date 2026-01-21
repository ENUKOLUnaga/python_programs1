import re
text="Python is a Programming Python language"
pattern=r"Python"
match=re.match(pattern,text)
print(match.span())
print(text[match.start():match.end():])
pattern2=r"language"
match=re.search(pattern2,text)
print(match.span())
print(text[match.start():match.end():])
#findall
pattern3=r"Python"
match=re.findall(pattern3,text)
print(match)
pattern4="Python|language"
match=re.findall(pattern4,text)
print(match)
text2="A whole is hole in wwwhole"
pattern5=r"w*hole"#*for 0 (or) many occurences
match=re.findall(pattern5,text2)
print(match)
pattern6=r"w?hole"#?for 0 (or) 1 occurences
match=re.findall(pattern6,text2)
print(match)
pattern7=r"w+hole"#+for 1 (or) more occurences
match=re.findall(pattern7,text2)
print(match)
text3="I know no one is there now"
pattern8=r"k?now?"
match=re.findall(pattern8,text3)
print(match)
print("Number of occurences: ",len(match))
#{} understanding
text4='''
gogle,
google,
gooogle,
goooogle
gooooogle'''
pattern9=r"go{2}gle"
match=re.findall(pattern9,text4)
print(match)
#understanding ^ and $ 
text5="python is not a snake python"
pattern10=r"^python"
pattern11=r"python$"
match=re.search(pattern10,text5)
print(match)
match=re.search(pattern11,text5)
print(match)
#understanding \w
text6="my name is ram : 1234567889"
pattern12=r"[a-z]"
match=re.findall(pattern12,text6)
print(match)
pattern13=r"[^a-z]"
match=re.findall(pattern13,text6)
print(match)
pattern14=r"\w"
match=re.findall(pattern14,text6)
print(match)
pattern15=r"\W"
match=re.findall(pattern15,text6)
print(match)
pattern16=r"([a-z])"
match=re.findall(pattern16,text6)
print(match)
text7="if tooth becomes teeth foot becomes feet"
pattern17="[aeiou]{2}"
match=re.findall(pattern17,text7)
print(match)
tex="2025/02/12"
pat=r"[/:-]"
l=re.split(pat,tex)
print(l)
