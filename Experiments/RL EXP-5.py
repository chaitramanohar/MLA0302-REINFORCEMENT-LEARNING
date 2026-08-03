import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\taxi.csv")

total_reward = 0

print("Taxi Dispatch System\n")

for index, row in data.iterrows():

    print(f"Location : {row['Location']}")

    if row['Pickup'] == "Yes":
        print("Passenger Picked Up")
        total_reward += row['Reward']

    else:
        print("No Pickup")
        total_reward += row['Reward']

    print()

print("Total Reward =", total_reward)
