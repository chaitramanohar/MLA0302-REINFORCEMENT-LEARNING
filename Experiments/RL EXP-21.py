import numpy as np
import matplotlib.pyplot as plt

# True click probabilities of 5 contents
probabilities = [0.2, 0.5, 0.3, 0.7, 0.4]

n_arms = len(probabilities)
counts = np.zeros(n_arms)
rewards = np.zeros(n_arms)

total_reward = []
T = 500

for t in range(1, T + 1):

    # Select each content once initially
    if t <= n_arms:
        arm = t - 1
    else:
        ucb = rewards / counts + np.sqrt(2 * np.log(t) / counts)
        arm = np.argmax(ucb)

    # Generate user feedback
    reward = np.random.rand() < probabilities[arm]

    counts[arm] += 1
    rewards[arm] += reward

    total_reward.append(reward)

print("Content selections:", counts.astype(int))
print("Estimated probabilities:", rewards / counts)

# Cumulative reward
plt.plot(np.cumsum(total_reward))
plt.xlabel("Rounds")
plt.ylabel("Cumulative Reward")
plt.title("UCB - Streaming Content Selection")
plt.show()
