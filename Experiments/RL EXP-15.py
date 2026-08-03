import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\callcenter.csv")

total = 0

print("Call Center\n")

for index, row in data.iterrows():

    print("Agent :", row["Agent"])
    print("Call Time :", row["CallTime"])

    total += row["CallTime"]

    print()

average = total / len(data)

print("Average Call Time =", average)
