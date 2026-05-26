import pandas as pd

df = pd.read_csv('customers.csv')
print(df.iloc[99])
print(df.to_string())

df1 = pd.read_json('p3.json')
print(df1.to_string())