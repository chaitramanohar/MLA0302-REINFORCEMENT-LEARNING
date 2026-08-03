import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\pricing.csv")

best_price = 0
max_revenue = 0

print("Pricing Strategies\n")

for index, row in data.iterrows():

    print(f"Price : {row['Price']}")
    print(f"Revenue : {row['Revenue']}")

    if row['Revenue'] > max_revenue:
        max_revenue = row['Revenue']
        best_price = row['Price']

    print()

print("Best Price =", best_price)
print("Maximum Revenue =", max_revenue)
