import pandas as pd

df = pd.read_csv('orders.csv')

df['CustomerName'] = df['CustomerName'].fillna('Unknown')

df['Quantity'].fillna(0)
df['Price'].fillna(0)

df['TotalAmount'] = df['Quantity'] * df['Price']

df.to_csv('orders_cleaned.csv', index=False)