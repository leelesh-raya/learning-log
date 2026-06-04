import pandas as pd

employees = pd.DataFrame(
    {
        "emp_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Carol", "Dave"],
        "dept_id": [101, 102, 104, 103],
    }
)

departments = pd.DataFrame(
    {"dept_id": [101, 102, 101], "dept_name": ["Engineering", "Marketing", "HR"]}
)

# on specifies which common column to refer while macthing
# Not using on by default refers all common columns for matching
df = pd.merge(employees, departments, on="dept_id")
print(df)

# how = inner keeps only matched rows
# when how is not used by default inner join is used
df = pd.merge(employees, departments, on="dept_id", how="inner")
print(df)

# how='outer' keeps all rows from both tables.
# Rows are matched using columns specified in `on`.
# Unmatched rows are also preserved with NaN values.
df = pd.merge(employees, departments, on="dept_id", how="outer")
print(df)

# how='left' keeps:
# 1. all rows from left table
# 2. only matched rows from right table
df = pd.merge(employees, departments, on="dept_id", how="left")
print(df)

# how='right' keeps:
# 1. all rows from right table
# 2. only matched rows from left table
df = pd.merge(employees, departments, on="dept_id", how="right")
print(df)

# how = 'left_anti' keeps only 'Unmatched rows' from 'Left table'
df = pd.merge(employees, departments, on="dept_id", how="left_anti")
print(df)

# how = 'right_anti' keeps only 'Unmatched rows' from 'right table'
df = pd.merge(employees, departments, on="dept_id", how="right_anti")
print(df)

# Also left_anti
df = pd.merge(employees, departments, how="outer", indicator=True)
left_anti = df[df['_merge']=='left_only'].drop(columns='_merge')
print(left_anti)