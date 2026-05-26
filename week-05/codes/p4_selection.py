import pandas as pd

df = pd.read_csv('customers.csv',encoding="utf-8-sig", index_col='First_name')

# Column selection
#print(df['First_name'].to_string())
#print(df[['First_name','Phone 1','Subscription Date']].to_string())


# Row selection
#print(df.loc[78:79]) # returns two rows
#print(df.iloc[78:79]) # return one row

# Row x Column selection
print(df.loc[['Maxwell','Caroline'], ['Customer Id' , 'Company','Email']])
print(df.loc['Maxwell':'Colleen', ['Customer Id' , 'Company','Email']])
print(df.iloc[55:74, 3:6])