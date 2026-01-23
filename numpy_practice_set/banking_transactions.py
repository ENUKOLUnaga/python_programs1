import numpy as np
def transactionAnalysis(transaction_amount):
    debit=np.where(transaction_amount<0,transaction_amount,0)
    credit=np.where(transaction_amount>0,transaction_amount,0)
    print("debit= ",debit)
    print("credit=",credit)
    daily_net_balance=transaction_amount.mean(axis=1)
    print(daily_net_balance)
    continuous_negative_values=np.where((transaction_amount<0).all(axis=0))[0]
    print(continuous_negative_values)

def main():
    transaction_amount=np.random.randint(-100,100,size=(20,50))
    print(transaction_amount)
    transactionAnalysis(transaction_amount)
if __name__=="__main__":
    main()