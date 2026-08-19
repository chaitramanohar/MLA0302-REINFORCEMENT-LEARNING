import numpy as np
import matplotlib.pyplot as plt

np.random.seed(8)

days = 100

water = 100
water_history = []
rewards = []

for day in range(days):

    demand = np.random.randint(5, 15)

    # Sustainable policy
    if water > 60:
        usage = demand
    elif water > 30:
        usage = min(demand, 8)
    else:
        usage = min(demand, 5)

    water -= usage

    # Natural replenishment
    water += 3

    water = np.clip(water, 0, 100)

    reward = usage - 0.1 * max(0, 50 - water)

    water_history.append(water)
    rewards.append(reward)

print("Average Reward:",
      round(np.mean(rewards), 2))

print("Final Water Level:",
      round(water, 2))

plt.plot(water_history)

plt.xlabel("Day")
plt.ylabel("Water Level")
plt.title("Sustainable Water Resource Management")
plt.grid()
plt.show()
