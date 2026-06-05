import pandas as pd

# join() matches using index

students = pd.DataFrame(
    {"id": [101, 102, 103], "name": ["Ram", "Sam", "chom"]}, index=[101, 102, 103]
)

marks = pd.DataFrame({"id": [101, 102], "math": [95, 88]}, index=[101, 102])


# by default it matches left index with right index and how = left
df = students.join(marks, rsuffix = "_students")
print(df)

# If 'on=' is used to specify the matching column, it matches left column with right 'index' only
# left 'id' is matched with right 'index' but not right 'id'
df = students.join(marks, on="id", how="outer" , rsuffix = "_students" )
print(df)
