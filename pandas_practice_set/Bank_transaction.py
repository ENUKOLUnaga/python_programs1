import pandas as pd
def bankTransaction(df):
    #sum of daily transaction per account
    sum_daily_transaction=df.groupby('account_id')['amount'].sum().reset_index()
    print(sum_daily_transaction)
    print(df)
    #high total transaction amount
    mean=sum_daily_transaction["amount"].mean()
    std=sum_daily_transaction["amount"].std()
    sum_daily_transaction['z_score']=(sum_daily_transaction['amount']-mean)/std
    high_amount=sum_daily_transaction[sum_daily_transaction["z_score"]>2]
    print(high_amount)
    #detect flag amount
    df["amount_zscore"]=(df["amount"]-df["amount"].mean())/df["amount"].std()
    df_fraud_amount=df[df["amount_zscore"]>3]
    print(df_fraud_amount)

def main():
    #reading data from csv
    df=pd.read_csv(r"C:\Users\ENKOL\PyCharmMiscProject\pandas_practice_set\data.csv")
    #print(df)
    bankTransaction(df)
if __name__=="__main__":
    main()