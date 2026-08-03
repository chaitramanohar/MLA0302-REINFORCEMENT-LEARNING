import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\calls.csv")

total = 0

print("Call Center\n")

for index, row in data.iterrows():

    print(f"Call ID : {row['CallID']}")
    print(f"Handling Time : {row['HandlingTime']}")

    total += row['HandlingTime']

    print()

average = total / len(data)

print("Average Handling Time =", average)
