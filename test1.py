import pandas as pd

df = pd.read_excel('inventory.xlsx')

df_cleaned = df.dropna(how='all')

df_cleaned.to_excel('cleaned_inventory.xlsx', index=False)

