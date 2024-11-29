import pandas as pd

df = pd.read_excel('inventory.xlsx')

incomplete_production_df = df[df['Production'] == 1]

top_10_products = incomplete_production_df['CAI'].value_counts().head(10)

print(top_10_products)
