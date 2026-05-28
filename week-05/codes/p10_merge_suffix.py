import pandas as pd

current = pd.DataFrame({
    'id': [1, 2],
    'salary': [50000, 60000]
})

old = pd.DataFrame({
    'id': [1, 2],
    'salary': [45000, 55000]
})

df = pd.merge(current, old, on='id', suffixes=('_current', '_old'))
print(df)