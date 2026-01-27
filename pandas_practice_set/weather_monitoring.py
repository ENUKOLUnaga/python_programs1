import pandas as pd
def weatherAnalysis(data):
    df=pd.DataFrame(data)
    print(df)
    #filter data based on one city
    city_name="New York"
    filtered_df=df.loc[df['city']==city_name]
    print(filtered_df)
    df["date"]=pd.to_datetime(df["date"])
    #average 3-day temperature
    df["rolling_average_temparature"]=df["temperature"].rolling(window=3).mean()
    #detecting days where humidity increased
    df["humidity"]=df["humidity"].diff()>0
    print(df)


def main():
    data={
    "date": ["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-02"],
    "city": ["New York", "New York", "London", "London"],
    "temperature": [30, 32, 45, 44],
    "humidity": [55, 50, 70, 78]
    }
    weatherAnalysis(data)
if __name__=="__main__":
    main()