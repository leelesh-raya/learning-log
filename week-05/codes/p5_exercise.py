import pandas as pd

df = pd.read_csv('customers.csv', index_col="First_name")

First_name = input('Enetr First_name:')

try:
    print(df.loc[First_name])
except KeyError:
    print('First_name not found')