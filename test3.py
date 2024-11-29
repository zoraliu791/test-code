import pandas as pd

df = pd.read_excel('inventory.xlsx')

result = df[df['Stock'] < 4].sort_values(by='Stock').head(5)

print(result)
