import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\stock_prices.csv")

profit = 0

print("Stock Trading\n")

buy_price = data.loc[0, "Price"]

for index, row in data.iterrows():

    print("Price =", row["Price"])

    if row["Price"] > buy_price:
        profit = row["Price"] - buy_price

print("\nTotal Profit =", profit)
