import pandas as pd

customers = pd.DataFrame(
    {"cust_id": [101, 102, 103, 104], "name": ["Ram", "Sam", "Asha", "Kiran"]}
)

orders = pd.DataFrame(
    {
        "customer_id": [101, 101, 103, 105],
        "product": ["Laptop", "Mouse", "Phone", "Tablet"],
    }
)

df = pd.merge(
    customers,
    orders,
    left_on="cust_id",
    right_on="customer_id",
    how="outer",
    indicator=True,
)
print(df)

non_buyers = df[df["_merge"] == "left_only"].drop(columns="_merge")
print(non_buyers)

orders_without_customer = df[df["_merge"] == "right_only"].drop(columns="_merge")
print(orders_without_customer)