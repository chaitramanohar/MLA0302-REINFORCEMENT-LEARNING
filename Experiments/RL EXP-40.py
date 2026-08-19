import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

grid_size = 10

robot = np.array([0, 0])
goal = np.array([9, 9])

path = [robot.copy()]

for step in range(50):

    # Limited observation:
    # robot only knows relative direction to goal
    observation = goal - robot

    if abs(observation[0]) > abs(observation[1]):
        action = np.array([
            np.sign(observation[0]), 0
        ])
    else:
        action = np.array([
            0, np.sign(observation[1])
        ])

    robot += action

    robot = np.clip(
        robot, 0, grid_size - 1
    )

    path.append(robot.copy())

    if np.array_equal(robot, goal):
        print("Robot reached the goal!")
        break

path = np.array(path)

plt.plot(
    path[:, 0],
    path[:, 1],
    marker="o"
)

plt.scatter(
    goal[0], goal[1],
    s=150,
    label="Goal"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("POMDP Robot Navigation")
plt.legend()
plt.grid()
plt.show()
