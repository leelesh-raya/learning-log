import pandas as pd

students = pd.DataFrame({
    'inde': [101, 102, 103],
    'name': ['Ram', 'Sam', 'chom']
}, index=[101, 102, 103])

marks = pd.DataFrame({
    'indec': [101, 102],
    'math': [95, 88]
}, index=[101, 102])

df = students.join(marks, on='inde', how='outer' )
print(df)