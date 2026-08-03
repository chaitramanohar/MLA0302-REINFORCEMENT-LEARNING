import pandas as pd

# Read the dataset
data = pd.read_csv(r"C:\Users\chait\Downloads\RL_Datasets\road.csv")

print("Autonomous Car Navigation\n")

for index, row in data.iterrows():

    print(f"Intersection : {row['Intersection']}")

    if row['TrafficLight'] == "Red":
        print("Stop")

    elif row['Destination'] == "Yes":
        print("Destination Reached")

    else:
        print("Move Forward")

    print()
