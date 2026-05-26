import pandas as pd

data = {
    "Name": ["Modi", "Trump", "Elon"],
    "Age": [75, 79, 54],
    "" "Job": ["PM", "President", "Alien"],
}

df = pd.DataFrame(data, index=["employee 1", "employee 2", "employee 3"])

# Add new column
df["weight"] = ["72", "83", "87"]

# Add new row
new_row = pd.DataFrame(
    [
        {"Name": "Hamza", "Age": 32, "Job": "N/A", "weight": 92},
        {"Name": "Jaskirat", "Age": 32, "Job": "soldier", "weight": 92},
    ],
    index=["employee 4", "employee 5"],
)
df = pd.concat([df, new_row])

print(df)
