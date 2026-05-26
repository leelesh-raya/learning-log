import pandas as pd

data = [100, 101, 102, 103]

series = pd.Series(data, index=['a','b', 'c', 'd'])

series['a'] += 200 # add in-place 
series['e'] = 200  # add new row

print(series.loc['a']) # print by index name
print(series.iloc[3]) # print by index order
print(series['c']) # print by index name
print(series[series>=102]) # Bool masking
