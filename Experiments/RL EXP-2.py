import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\warehouse.csv")

total_value = 0

print("Warehouse Navigation\n")

for index, row in data.iterrows():

    print(f"State : {row['State']}")

    if row['Obstacle'] == 1:
        print("Obstacle Hit")
        value = row['Reward'] - 2

    elif row['Goal'] == 1:
        print("Goal Reached")
        value = row['Reward'] + 5

    else:
        print("Moving")
        value = row['Reward']

    print("State Value =", value)
    total_value += value
    print()

print("Total Value Function =", total_value)
