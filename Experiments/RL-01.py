import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\grid.csv")

reward = 0

print("Robot Navigation\n")

for index, row in data.iterrows():

    print(f"Cell ({row['Row']},{row['Col']})")

    if row['Obstacle'] == 1:
        print("Obstacle Found")
        reward -= 1

    elif row['Dirt'] == 1:
        print("Dirt Cleaned")
        reward += 1

    else:
        print("Empty Cell")

print("\nTotal Reward =", reward)
