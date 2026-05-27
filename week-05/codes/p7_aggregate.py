import pandas as pd

# Aggregate functions = Used to summarize and analyze data

df = pd.read_csv('pokemon.csv')
# Calculate mean for whole df
print(df.mean(numeric_only=True)) # This argument prevents error by dropping non-numerical columns

# Applying aggregate func to a column
print(df['Height'].mean()) 
print(df['Height'].sum())
print(df['Height'].max())
print(df['Height'].min())
print(df['Height'].count())


# What if we have to group rows with similar properties and apply calculations on these different groups?
group = df.groupby('Type1') # this will make groups pokemons with similar type1


# Calculating metrics per group
print(group['Height'].mean()) # Calculate avg height for each group
print(group['Height'].sum())
print(group['Height'].max())
print(group['Height'].min())
print(group['Height'].count())