class DuplicateUserError(Exception):
    pass
class WeakPasswordError(Exception):
    pass
class User:
    user_names=set()
    def __init__(self,username,mblnumber,password):
        self.username=username
        self.mblnumber=mblnumber
        self.password=password
        self.add_user()
        self.Validate()


    def add_user(self):
        if self.username in User.user_names:
            raise DuplicateUserError("User already Exists")
        else:
            User.user_names.add(self.username)
    def Validate(self):
        uc=lc=dc=sc=0
        for i in self.password:
            if i.isupper():
                uc+=1
            elif i.islower():
                lc+=1
            elif i.isdigit():
                dc+=1
            else:
                sc+=1
        if len(self.password)<8 or uc==0 or lc==0 or dc==0 or sc==0:
            raise WeakPasswordError("Password not acceptable")
def main():
    username=input("Enter a Username: ")
    mblnumber=int(input("enter mobile number: "))
    password=input("Enter a password")

    try:
        u1=User(username,mblnumber,password)
    except DuplicateUserError as e:
        print(e)
    except WeakPasswordError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print("Account Created Successfully")
main()
    

        