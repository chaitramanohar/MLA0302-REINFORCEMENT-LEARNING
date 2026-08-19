import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

start = np.array([5, 5])
goal = np.array([95, 95])

obstacles = [
    (20, 20, 20, 50),
    (50, 10, 15, 40),
    (60, 60, 25, 15),
    (20, 75, 30, 10)
]

step_size = 5
max_iterations = 2000

nodes = [start]
parents = [-1]


def collision(point):
    x, y = point

    for ox, oy, w, h in obstacles:
        if ox <= x <= ox + w and oy <= y <= oy + h:
            return True

    return False


for _ in range(max_iterations):

    random_point = np.random.uniform(0, 100, 2)

    distances = [np.linalg.norm(n - random_point) for n in nodes]
    nearest_index = np.argmin(distances)

    nearest = nodes[nearest_index]

    direction = random_point - nearest
    direction = direction / (np.linalg.norm(direction) + 1e-8)

    new_point = nearest + step_size * direction

    if not collision(new_point):
        nodes.append(new_point)
        parents.append(nearest_index)

        if np.linalg.norm(new_point - goal) < 7:
            print("Goal reached!")
            break

# Plot
plt.figure(figsize=(8, 8))

for ox, oy, w, h in obstacles:
    plt.gca().add_patch(
        plt.Rectangle((ox, oy), w, h, color="gray")
    )

for i in range(1, len(nodes)):
    p = parents[i]
    plt.plot(
        [nodes[i][0], nodes[p][0]],
        [nodes[i][1], nodes[p][1]],
        "b-",
        alpha=0.5
    )

plt.scatter(*start, c="green", s=100, label="Start")
plt.scatter(*goal, c="red", s=100, label="Goal")

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("RRT Path Planning for Exploration Robot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
