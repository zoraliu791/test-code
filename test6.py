import pandas as pd

df = pd.read_excel('inventory.xlsx')

average_stock = df.groupby(['Warehouse', 'Product'])['Stock'].mean().reset_index()

print(average_stock)