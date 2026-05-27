import pandas as pd

# Data Cleaning
df = pd.read_csv("pokemon.csv")

print(df.shape) # confirm the change happened correctly.
df.info() # prints a summary of the DataFrame

# 1. Drop irrevelant column or row
# df = df.drop(columns=['Legendary', 'No'])
# df = df.drop(index=0)

# 2. Handling missing data
# df = df.dropna(subset=['Type2']) # If Type2 column of a row is missing a data the row is dropped
df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE"})

# 4. Standardize text
df["Name"] = df["Name"].str.upper()

# 5. Change dtype
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Drop duplicate rows
df = df.drop_duplicates()

print(df.shape)
 
print(df.to_string())
