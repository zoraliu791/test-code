import pandas as pd

df = pd.read_excel('inventory.xlsx')

order_us = pd.read_csv('order_us.csv')
order_eu = pd.read_csv('order_eu.csv')

merged_orders = pd.merge(order_us, order_eu, on='Order_ID', how='outer', suffixes=('_us', '_eu'))

print(merged_orders)
