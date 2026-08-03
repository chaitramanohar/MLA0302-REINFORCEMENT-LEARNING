import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\portfolio.csv")

total_return = 0

print("Portfolio Management\n")

for index, row in data.iterrows():

    print("Stock :", row["Stock"])
    print("Return :", row["Return"])
    print("Risk :", row["Risk"])

    total_return += row["Return"]

    print()

print("Total Return =", total_return)
