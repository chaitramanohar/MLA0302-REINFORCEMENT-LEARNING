import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

days = 100

# Generate customer demand
demand = np.random.poisson(5, days)

inventory = 10

costs = []
inventory_history = []

# Policy 1: Fixed order policy
for day in range(days):

    if inventory < 5:
        inventory += 10

    sales = min(inventory, demand[day])

    holding_cost = 0.5 * inventory
    shortage_cost = 2 * max(0, demand[day] - inventory)

    total_cost = holding_cost + shortage_cost

    inventory -= sales

    costs.append(total_cost)
    inventory_history.append(inventory)

print("Average Inventory Cost:",
      round(np.mean(costs), 2))

plt.plot(inventory_history)
plt.xlabel("Day")
plt.ylabel("Inventory")
plt.title("Inventory Dynamics")
plt.grid()
plt.show()
