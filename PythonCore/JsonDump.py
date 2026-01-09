import json
books={}
books["tom"]={
    "name":"Tom",
    "address":"123 red st.xavior",
    "ph_number":4567894561

}
books["heb"]={
    "name":"heb",
    "address":"123 green st.xavior",
    "ph_number":1234567891

}
"""print(books)
s=json.dumps(books)
print(s)
with open("datajson.txt","w") as f:
    f.write(s)
f.close"""
with open(r"C:\Users\ENKOL\PyCharmMiscProject\datajson.txt", "r") as f:
    s = json.load(f)   
    print(s)
    print(type(s))
f.close()
    
