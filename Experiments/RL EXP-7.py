import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\warehouse_states.csv")

print("State Value Function\n")

for index, row in data.iterrows():

    value = row['Reward'] + 1

    print(f"State : {row['State']}")
    print("Value =", value)
    print()
