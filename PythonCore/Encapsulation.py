class Account:
    def __init__(self):
        self.__balance=10000
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>0:
            self.__balance=balance
        else:
            print("balance must be greater than 0")
    ac=property(get_balance,set_balance)

ac1=Account()
#print(ac1.__dict__)
ac1.ac=100
print(ac1.ac)

