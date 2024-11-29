import pandas as pd

data = {
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
    'Delivery_Time': [3, 6, 9]
}

df = pd.DataFrame(data)


def classify_delivery_time(delivery_time):
    if delivery_time < 5:
        return 'Fast'
    elif delivery_time > 10:
        return 'Slow'
    else:
        return 'Normal'


df['Status'] = df['Delivery_Time'].apply(classify_delivery_time)

print(df)