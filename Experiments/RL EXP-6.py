import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\ads.csv")

best_ad = ""
max_clicks = 0

print("Advertisement Performance\n")

for index, row in data.iterrows():

    print(f"Ad : {row['Ad']}")
    print(f"Clicks : {row['Clicks']}")

    if row['Clicks'] > max_clicks:
        max_clicks = row['Clicks']
        best_ad = row['Ad']

    print()

print("Best Advertisement =", best_ad)
print("Maximum Clicks =", max_clicks)
