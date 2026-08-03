import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\stocks.csv")

profit = 0

print("Investment Strategy\n")

for index, row in data.iterrows():

    print(f"Day : {row['Date']}")

    gain = row['Close'] - row['Open']

    print("Profit =", gain)

    profit += gain

    print()

print("Total Profit =", profit)
