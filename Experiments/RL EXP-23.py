import numpy as np
import matplotlib.pyplot as plt

grid_size = 4
gamma = 0.9

# Terminal state
goal = (3, 3)

# Actions
actions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

# Random policy
policy = np.ones((grid_size, grid_size, 4)) / 4

value = np.zeros((grid_size, grid_size))

# Value iteration
for iteration in range(100):

    new_value = np.zeros_like(value)

    for r in range(grid_size):
        for c in range(grid_size):

            if (r, c) == goal:
                continue

            values = []

            for action in actions.values():

                nr = r + action[0]
                nc = c + action[1]

                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    reward = 1 if (nr, nc) == goal else -0.1
                    values.append(reward + gamma * value[nr, nc])
                else:
                    values.append(-1 + gamma * value[r, c])

            new_value[r, c] = max(values)

    value = new_value

print("Value Function:")
print(np.round(value, 2))

plt.imshow(value, cmap="viridis")
plt.colorbar(label="Value")
plt.title("Gridworld Value Function")
plt.xlabel("Column")
plt.ylabel("Row")
plt.show()
