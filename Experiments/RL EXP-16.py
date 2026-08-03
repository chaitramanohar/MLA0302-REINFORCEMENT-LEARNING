import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\energy.csv")

total_cost = 0

print("Smart Grid Energy Management\n")

for index, row in data.iterrows():

    print("Demand :", row["Demand"])
    print("Supply :", row["Supply"])

    if row["Supply"] >= row["Demand"]:
        print("Energy Balanced")
    else:
        print("Energy Shortage")

    total_cost += row["Cost"]
    print()

print("Total Cost =", total_cost)
