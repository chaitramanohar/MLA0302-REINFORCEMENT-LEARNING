import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\gridworld.csv")

steps = 0

print("GridWorld Navigation\n")

for index, row in data.iterrows():

    print(f"Position ({row['Row']},{row['Col']})")

    if row["Obstacle"] == 1:
        print("Obstacle Found")

    elif row["Goal"] == 1:
        print("Goal Reached")
        steps += 1

    else:
        print("Moving")
        steps += 1

    print()

print("Total Steps =", steps)
