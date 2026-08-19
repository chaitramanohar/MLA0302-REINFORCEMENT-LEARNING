import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

actions = ["Action A", "Action B"]

rewards = []
fairness_scores = []

for episode in range(100):

    group = np.random.choice(
        ["Group 1", "Group 2"]
    )

    # Simulated action scores
    score_a = np.random.rand()
    score_b = np.random.rand()

    # Ethical penalty
    if group == "Group 1":
        score_a -= 0.2

    if group == "Group 2":
        score_b -= 0.2

    # Fairness-aware decision
    if abs(score_a - score_b) < 0.1:
        action = np.random.choice(actions)
    else:
        action = actions[
            np.argmax([score_a, score_b])
        ]

    reward = max(score_a, score_b)

    rewards.append(reward)

    fairness = 1 - abs(score_a - score_b)
    fairness_scores.append(fairness)

print("Average Reward:",
      round(np.mean(rewards), 3))

print("Average Fairness:",
      round(np.mean(fairness_scores), 3))

plt.plot(rewards, label="Reward")
plt.plot(fairness_scores, label="Fairness")

plt.xlabel("Episode")
plt.ylabel("Score")
plt.title("Ethical Reinforcement Learning")
plt.legend()
plt.grid()
plt.show()
