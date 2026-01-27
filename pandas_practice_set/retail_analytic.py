import pandas as pd

data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "customer_id": [1, 2, 5, 3, 6, 7, 4, 3],
    "order_date": [
        "2025-01-01", "2025-01-02", "2025-01-05", "2025-01-07",
        "2025-01-10", "2025-02-15", "2025-01-18", "2025-01-20"
    ],
    "order_amount": [250, 400, 150, 300, 500, 200, 450, 350]
}

df = pd.DataFrame(data)
#convert order_date to datetime
df['order_date'] = pd.to_datetime(df["order_date"])
print(df['order_date'])

#monthly total revenue
monthly_total=df.groupby(df['order_date'].dt.to_period('M'))['order_amount'].sum().reset_index(name='monthly_total_revenue')
print(monthly_total)

#highest number of unique customers
unique_customers_per_month=df.groupby(df['order_date'].dt.to_period('M'))['customer_id'].nunique().reset_index(name='unique_customers')
top_month=unique_customers_per_month.loc[unique_customers_per_month['unique_customers'].idxmax()]
print(top_month)