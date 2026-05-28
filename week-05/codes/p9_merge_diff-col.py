import pandas as pd


# Used when matching columns have different names ('emp_id'='worker_id')
employees = pd.DataFrame({
    'emp_id': [1, 2],
    'name': ['Ram', 'Sam']
})

salaries = pd.DataFrame({
    'worker_id': [1, 2],
    'salary': [50000, 60000]
})

df = pd.merge(employees, salaries, left_on='emp_id', right_on='worker_id')
print(df)