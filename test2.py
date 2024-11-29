import pandas as pd

df = pd.read_excel('inventory.xlsx')

df_cleaned = df.drop_duplicates(subset='ProductID', keep='first')

df_cleaned.to_excel('cleaned_inventory_no_duplicates.xlsx', index=False)
