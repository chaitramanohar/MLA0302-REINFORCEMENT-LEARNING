import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\grid_game.csv")

reward = 0

print("Grid Game\n")

for index, row in data.iterrows():

    print("Cell :", row["Cell"])

    reward += row["Reward"]

    print("Reward =", row["Reward"])
    print()

print("Total Reward =", reward)
