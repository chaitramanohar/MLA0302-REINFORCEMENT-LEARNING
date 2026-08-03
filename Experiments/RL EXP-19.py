import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\resources.csv")

print("Game Resources\n")

for index, row in data.iterrows():

    print("Wood :", row["Wood"])
    print("Gold :", row["Gold"])
    print("Food :", row["Food"])
    print("Enemy :", row["Enemy"])
    print("Resources Collected Successfully\n")
