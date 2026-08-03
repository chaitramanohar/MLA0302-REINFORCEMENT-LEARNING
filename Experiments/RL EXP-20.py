import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\racing.csv")

total_reward = 0

print("Autonomous Vehicle Racing\n")

for index, row in data.iterrows():

    print("Lap :", row["Lap"])
    print("Speed :", row["Speed"])
    print("Reward :", row["Reward"])

    total_reward += row["Reward"]

    print()

print("Total Reward =", total_reward)
