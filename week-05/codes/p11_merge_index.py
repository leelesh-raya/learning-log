import pandas as pd

students = pd.DataFrame({
    'name': ['Ram', 'Sam']
})

marks = pd.DataFrame({
    'math': [95, 88]
})

df = pd.merge(students, marks, left_index=True, right_index=True)
print(df)