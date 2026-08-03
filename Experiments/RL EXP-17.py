import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\movies.csv")

print("Recommended Movies\n")

for index, row in data.iterrows():

    if row["Rating"] >= 4:
        print(row["Movie"], "- Recommended")
    else:
        print(row["Movie"], "- Not Recommended")
