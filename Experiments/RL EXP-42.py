import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

patients = 100

waiting_time = np.random.randint(
    1, 10, patients
)

resources = 5

rewards = []

for episode in range(100):

    total_reward = 0

    for patient in range(patients):

        wait = waiting_time[patient]

        # RL-style decision
        if wait > 5:
            priority = True
        else:
            priority = False

        if priority:
            treatment_time = 1
            reward = 10 - wait
        else:
            treatment_time = 2
            reward = 5 - wait

        # Resource penalty
        if treatment_time > resources:
            reward -= 5

        total_reward += reward

    rewards.append(total_reward)

print("Average Healthcare Reward:",
      round(np.mean(rewards), 2))

plt.plot(rewards)

plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Healthcare Management Optimization")
plt.grid()
plt.show()
