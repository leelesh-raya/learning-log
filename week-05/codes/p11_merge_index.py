import pandas as pd

# Use when the indexes themselves represent the relationship between tables

students = pd.DataFrame({
    'name': ['Ram', 'Sam']
})

marks = pd.DataFrame({
    'math': [95, 88]
})

df = pd.merge(students, marks, left_index=True, right_index=True)
print(df)