import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)

days = 100

demand = np.random.poisson(8, days)

inventory = 20
orders = []
costs = []

for day in range(days):

    # Reorder policy
    if inventory < 10:
        order = 20
    else:
        order = 0

    inventory += order

    sales = min(inventory, demand[day])

    inventory -= sales

    holding = inventory * 0.5
    shortage = max(0, demand[day] - sales) * 3
    transport = order * 0.2

    total_cost = holding + shortage + transport

    orders.append(order)
    costs.append(total_cost)

print("Average Supply Chain Cost:",
      round(np.mean(costs), 2))

plt.plot(np.cumsum(costs))

plt.xlabel("Day")
plt.ylabel("Cumulative Cost")
plt.title("Supply Chain Cost")
plt.grid()
plt.show()
