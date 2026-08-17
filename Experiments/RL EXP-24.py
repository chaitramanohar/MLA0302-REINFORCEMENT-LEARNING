import numpy as np

max_inventory = 5
max_order = 3

holding_cost = 1
order_cost = 2
shortage_cost = 5

gamma = 0.9

value = np.zeros(max_inventory + 1)
policy = np.zeros(max_inventory + 1)

for iteration in range(100):

    new_value = np.zeros_like(value)

    for inventory in range(max_inventory + 1):

        costs = []

        for order in range(max_order + 1):

            new_inventory = min(inventory + order, max_inventory)

            # Assume demand = 2
            demand = 2

            remaining = new_inventory - demand

            if remaining >= 0:
                cost = order_cost * order + holding_cost * remaining
            else:
                cost = order_cost * order + shortage_cost * abs(remaining)

            total_cost = cost + gamma * value[max(0, remaining)]
            costs.append(total_cost)

        best_action = np.argmin(costs)

        new_value[inventory] = costs[best_action]
        policy[inventory] = best_action

    value = new_value

print("Inventory Level | Optimal Order")
print("-------------------------------")

for i in range(max_inventory + 1):
    print(i, "              |", int(policy[i]))

print("\nMinimum Cost:")
print(np.round(value, 2))
