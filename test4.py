import pandas as pd
from datetime import datetime, timedelta

df = pd.read_excel('inventory.xlsx')

df['Last_Update'] = pd.to_datetime(df['Last_Update'], format='%Y-%m-%d')

today = datetime.now()

thirty_days_ago = today - timedelta(days=30)

recently_updated_products = df[df['Last_Update'] >= thirty_days_ago]

total_stock = recently_updated_products['Stock'].sum()

print(total_stock)