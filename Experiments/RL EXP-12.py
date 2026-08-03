import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\rooms.csv")

reward = 0

print("Robot Vacuum Cleaner\n")

for index, row in data.iterrows():

    print("Room :", row["Room"])

    if row["Status"] == "Dirty":
        print("Cleaning Room")
        reward += 10

    elif row["Status"] == "Obstacle":
        print("Obstacle Found")
        reward -= 5

    else:
        print("Already Clean")

    print()

print("Total Reward =", reward)
