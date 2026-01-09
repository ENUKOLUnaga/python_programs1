import os
#removing files
if os.path.exists("name.txt"):
  os.remove("name.txt")
else:
  print("The file does not exist")
#Creating a File
#f1=open("name.txt","x")
#writing files
f1=open("names.txt","w")
f1.write("Hello")
f1.close()
#reading files
f1=open("names.txt","r")
print(f1.read())
f1.close()
#writting on files
f1=open("names.txt","a")
f1.write("\nThis is Over written file")
f1.close()
#tell() method
f1=open("names.txt","r")
print(f1.tell())
f1=open("names.txt","r")
print(f1.read())
f1.close()
#over written files
f1=open("names.txt","a")
f1.write("\nThis is Over written file")
f1.close()

f1=open("names.txt","r")
print(f1.read())
f1.close()
#reading line by line
file = open("names.txt", "r")
lines = file.readlines()
print(lines)
file.close()
#tell() method
f1=open("names.txt","r")
print(f1.tell())
#seek() method
with open("names.txt","r") as f1:
  f1.seek(5)
  print(f1)
#binary files 
with open("application.png", "rb") as src:
    with open("copy.jpg", "wb") as dest:
        dest.write(src.read())
