import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\city_grid.csv")

steps = 0

print("Delivery Drone Navigation\n")

for index, row in data.iterrows():

    print(f"Position ({row['X']},{row['Y']})")

    if row['Obstacle'] == 1:
        print("Obstacle Found")

    elif row['Goal'] == 1:
        print("Destination Reached")
        steps += 1

    else:
        print("Moving")
        steps += 1

    print()

print("Total Steps =", steps)
