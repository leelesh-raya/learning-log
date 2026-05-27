import pandas as pd, numpy as np

df = pd.read_csv("pokemon.csv")

psychic = df.loc[df['Weight']>=90 , ['Name','Weight']]
water_pokemon = df[(df['Type1']=='Water') | (df['Type2']=='Water')  ]
ff_pokemon = df[(df['Type1']=='Fire') &
                (df['Type2']=='Flying')]


print(psychic)
print(water_pokemon)
print(ff_pokemon)
