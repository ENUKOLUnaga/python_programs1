import numpy as np
def retailAnalysis(daily_sales):
    #cleaning data (negative values with zero)
    sales=np.where(daily_sales<0,0,daily_sales)
    print(sales)
    #average weekly sales per product
    temp=sales[:28]
    weekly_Data=temp.reshape(4,7,5)
    print("weekly data: ")
    print(weekly_Data)
    weekly_Sales=weekly_Data.sum(axis=1)
    print(weekly_Sales)
    average_Weekly_Sales=weekly_Sales.mean(axis=0)
    average_Weekly_Sales=average_Weekly_Sales.astype(int)
    print("avereage weekly sales: ",average_Weekly_Sales)
    #highest average weekly sales
    print("Highest weekly sales: ",np.max(average_Weekly_Sales))
def main():
    #getting 5 products for 30 days
    daily_sales=np.random.randint(-30,50,size=(30,5))
    print(daily_sales)
    retailAnalysis(daily_sales)
if __name__=="__main__":
    main()