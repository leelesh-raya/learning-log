import pandas as pd

df1 = pd.read_csv('pokemon.csv', index_col='Name')

df2 =  df1['Height']

df3 = df2.map(lambda x: 'taller' if x>6 else 'shorter')
print(df3.to_string())




df2 =  df1['Legendary']

# Using dictionaries
df4 = df2.map({
    1 : True,
    0 : False
})
print(df4.to_string())


# Note: map() works only for series