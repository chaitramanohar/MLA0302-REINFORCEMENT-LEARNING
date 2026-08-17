import numpy as np
import matplotlib.pyplot as plt

probabilities = [0.2, 0.5, 0.3, 0.7, 0.4]
n_arms = 5
T = 500
epsilon = 0.1


# ---------------- EPSILON GREEDY ----------------
def epsilon_greedy():

    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)
    total = []

    for t in range(T):

        if np.random.rand() < epsilon:
            arm = np.random.randint(n_arms)
        else:
            values = rewards / (counts + 1e-10)
            arm = np.argmax(values)

        reward = np.random.rand() < probabilities[arm]

        counts[arm] += 1
        rewards[arm] += reward
        total.append(reward)

    return np.cumsum(total)


# ---------------- UCB ----------------
def ucb():

    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)
    total = []

    for t in range(1, T + 1):

        if t <= n_arms:
            arm = t - 1
        else:
            values = rewards / counts
            confidence = np.sqrt(2 * np.log(t) / counts)
            arm = np.argmax(values + confidence)

        reward = np.random.rand() < probabilities[arm]

        counts[arm] += 1
        rewards[arm] += reward
        total.append(reward)

    return np.cumsum(total)


# ---------------- THOMPSON SAMPLING ----------------
def thompson_sampling():

    alpha = np.ones(n_arms)
    beta = np.ones(n_arms)
    total = []

    for t in range(T):

        samples = np.random.beta(alpha, beta)
        arm = np.argmax(samples)

        reward = np.random.rand() < probabilities[arm]

        if reward:
            alpha[arm] += 1
        else:
            beta[arm] += 1

        total.append(reward)

    return np.cumsum(total)


eg = epsilon_greedy()
ucb_result = ucb()
ts = thompson_sampling()

plt.plot(eg, label="Epsilon-Greedy")
plt.plot(ucb_result, label="UCB")
plt.plot(ts, label="Thompson Sampling")

plt.xlabel("Rounds")
plt.ylabel("Cumulative Reward")
plt.title("k-Armed Bandit Comparison")
plt.legend()
plt.show()
