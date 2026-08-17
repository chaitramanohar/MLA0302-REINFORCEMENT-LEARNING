import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# Actor network
actor = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(3,)),
    layers.Dense(32, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

# Critic network
critic = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(4,)),
    layers.Dense(32, activation="relu"),
    layers.Dense(1)
])

actor_optimizer = tf.keras.optimizers.Adam(0.001)
critic_optimizer = tf.keras.optimizers.Adam(0.001)

for episode in range(100):

    # User preference state
    state = np.random.rand(3).astype(np.float32)

    with tf.GradientTape() as tape_actor:

        action = actor(state.reshape(1, -1))[0][0]

        # Simulated user feedback
        reward = 1.0 - abs(action - state[0])

        loss_actor = -reward

    actor_grads = tape_actor.gradient(
        loss_actor, actor.trainable_variables
    )

    actor_optimizer.apply_gradients(
        zip(actor_grads, actor.trainable_variables)
    )

    if episode % 10 == 0:
        print("Episode:", episode,
              "Reward:", round(float(reward), 3))
