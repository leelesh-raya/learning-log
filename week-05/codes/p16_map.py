import pandas as pd

df1 = pd.read_csv('pokemon.csv', index_col='Name')

# create a Series 
df2 =  df1['Height']

# map() transforms each value in a Series using a dictionary, Series, or function and returns a new Series. 

df3 = df2.map(lambda x: 'taller' if x>6 else 'shorter')
print(df3.to_string())


# Using dictionaries
df2 =  df1['Legendary']

df4 = df2.map({
    1 : True,
    0 : False
})
print(df4.to_string())


# Note: map() works only for series