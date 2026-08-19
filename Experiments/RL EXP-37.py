import numpy as np

np.random.seed(1)

resources = 0
buildings = 0
total_reward = 0

episodes = 50

for episode in range(episodes):

    resources = 0
    buildings = 0
    reward = 0

    # MAXQ high-level task
    for step in range(20):

        # Subtask 1: Collect resources
        if resources < 3:
            resources += 1
            reward += 1

        # Subtask 2: Build structure
        elif buildings < 2:
            resources -= 3
            buildings += 1
            reward += 5

        # Main task completed
        else:
            reward += 10
            break

    total_reward += reward

    if episode % 10 == 0:
        print(
            "Episode:", episode,
            "Buildings:", buildings,
            "Reward:", reward
        )

print("\nAverage Reward:",
      total_reward / episodes)
