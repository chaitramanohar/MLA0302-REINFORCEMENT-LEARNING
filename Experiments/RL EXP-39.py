import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)

n_robots = 3
target = np.array([10, 10])

positions = np.random.randint(
    0, 5, (n_robots, 2)
)

rewards = []

for episode in range(100):

    positions = np.random.randint(
        0, 5, (n_robots, 2)
    )

    total_reward = 0

    for step in range(30):

        for i in range(n_robots):

            direction = target - positions[i]

            if abs(direction[0]) > abs(direction[1]):
                positions[i][0] += np.sign(direction[0])
            else:
                positions[i][1] += np.sign(direction[1])

            positions[i] = np.clip(
                positions[i], 0, 10
            )

        distance = np.mean(
            np.linalg.norm(
                positions - target,
                axis=1
            )
        )

        total_reward -= distance

        if distance < 1:
            total_reward += 100
            break

    rewards.append(total_reward)

print("Average Team Reward:",
      np.mean(rewards))

plt.plot(rewards)

plt.xlabel("Episode")
plt.ylabel("Team Reward")
plt.title("Multi-Agent Robot Cooperation")
plt.grid()
plt.show()
