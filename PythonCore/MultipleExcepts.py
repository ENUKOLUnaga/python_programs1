
class ItemNotPresentError(Exception):
    pass
def menu(item):
    if item=="idly":
        print("enjoy your idly")
    elif item=="pizza":
        print("enjoy your pizza")
    elif item=="Burger":
        print("enjoy your burger")
    else:
        raise ItemNotPresentError("Enter a valid Item")
def main():
    item=input("menu item: ")
    menu(item)
main()
"""
def menu(item):
    if item=="idly":
        print("enjoy your idly")
    elif item=="pizza":
        print("enjoy your pizza")
    elif item=="Burger":
        print("enjoy your burger")
    else:
        raise ValueError
def main():
    item=input("menu item: ")
    menu(item)
main()
    
  
print("Execution started")
list1=[10,20,0,40,50]
d={1:'c',2:'java',3:'python',4:'C++'}
try:
    n=int(input("Enter a key"))
    print(d[n])
    numerator=int(input("Enter numerator"))
    denominator=int(input("Enter Denominator"))
    res=list1[numerator]/list1[denominator]
    print(res)
except KeyError as e:
    print(e)
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
print("Execution Terminated")"""