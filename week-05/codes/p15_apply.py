import pandas as pd

df = pd.DataFrame({
    'math': [90, 80],
    'science': [70, 60]
})

def plus2(row):
    r = row+2
    return r

#apply() is used to apply a custom function to each element of a Series or to each row/column of a DataFrame.

print(df.apply(sum)) # across rows
print(df.apply(sum, axis=1)) # across columns
print(df['math'].apply(plus2)) # Applies plus2 function for each row along column 'math'
print(df['math'].sum()) # sums up entire math column, #170
plus3 = df['science'].apply(lambda x: x + 3)
print(plus3)