import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

energy_demand = np.random.randint(5, 15, 100)

# Initial policy
policy = np.ones(100) * 0.5

cost_before = []
cost_after = []

for i in range(100):

    demand = energy_demand[i]

    # Before optimization
    supplied = policy[i] * 20
    cost = abs(demand - supplied) + 0.1 * supplied
    cost_before.append(cost)

    # TRPO-like small policy update
    error = demand - supplied

    update = 0.01 * error

    # Restrict update (trust region)
    update = np.clip(update, -0.05, 0.05)

    policy[i] += update

    supplied = policy[i] * 20
    cost = abs(demand - supplied) + 0.1 * supplied

    cost_after.append(cost)

print("Average cost before:", np.mean(cost_before))
print("Average cost after :", np.mean(cost_after))

plt.plot(cost_before, label="Before TRPO")
plt.plot(cost_after, label="After TRPO")

plt.xlabel("Time")
plt.ylabel("Energy Cost")
plt.title("Smart Grid Cost Optimization")
plt.legend()
plt.show()
