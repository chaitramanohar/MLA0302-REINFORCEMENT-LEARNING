import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# Policy network
policy = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(3,)),
    layers.Dense(4, activation="softmax")
])

optimizer = tf.keras.optimizers.Adam(0.01)

for episode in range(200):

    state = np.random.rand(3).astype(np.float32)

    states = []
    actions = []
    rewards = []

    for step in range(10):

        probabilities = policy(
            state.reshape(1, -1)
        )

        action = np.random.choice(
            4,
            p=probabilities.numpy()[0]
        )

        # Simulated audience engagement
        reward = np.random.uniform(0, 1)

        states.append(state)
        actions.append(action)
        rewards.append(reward)

    # Calculate returns
    returns = []
    G = 0

    for reward in reversed(rewards):
        G = reward + 0.95 * G
        returns.insert(0, G)

    with tf.GradientTape() as tape:

        probabilities = policy(
            np.array(states)
        )

        loss = 0

        for i in range(len(actions)):

            loss -= tf.math.log(
                probabilities[i, actions[i]] + 1e-10
            ) * returns[i]

    gradients = tape.gradient(
        loss,
        policy.trainable_variables
    )

    optimizer.apply_gradients(
        zip(gradients, policy.trainable_variables)
    )

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "Engagement:",
            round(float(np.mean(rewards)), 3)
        )
