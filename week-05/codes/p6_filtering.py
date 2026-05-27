import pandas as pd, numpy as np

# Filtering = Keeping rows or columns that match a condition
df = pd.read_csv("pokemon.csv")


heavy = df.loc[df["Weight"] >= 90, ["Name", "Weight"]] # Use loc when dealing with index or more than one argument

# Keeping rows that match either of the conditions
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

# Kepping rows that match both conditions
ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
  

print(heavy)
print(water_pokemon)
print(ff_pokemon)

