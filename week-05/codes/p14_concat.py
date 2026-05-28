import pandas as pd

jan = pd.DataFrame({
    'product': ['Laptop', 'Mouse'],
    'sales': [10, 25]
})

feb = pd.DataFrame({
    'product': ['Phone', 'Keyboard'],
    'sales': [15, 12]
})

df = pd.concat([jan, feb], ignore_index=True, axis=0)
print(df)

df = pd.concat([jan, feb], ignore_index=True, axis=1)
print(df)