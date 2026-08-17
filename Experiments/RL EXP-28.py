import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

actor = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(4,)),
    layers.Dense(4, activation="softmax")
])

critic = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(4,)),
    layers.Dense(1)
])

actor_optimizer = tf.keras.optimizers.Adam(0.001)
critic_optimizer = tf.keras.optimizers.Adam(0.001)

for episode in range(100):

    # resources, buildings, army, enemy
    state = np.random.rand(4).astype(np.float32)

    with tf.GradientTape() as at, tf.GradientTape() as ct:

        probabilities = actor(state.reshape(1, -1))
        value = critic(state.reshape(1, -1))

        action = tf.random.categorical(
            tf.math.log(probabilities), 1
        )[0, 0]

        # Simulated strategic reward
        reward = np.random.choice([-1, 0, 1])

        advantage = reward - value[0, 0]

        actor_loss = -tf.math.log(
            probabilities[0, action]
        ) * advantage

        critic_loss = tf.square(advantage)

    actor_grad = at.gradient(
        actor_loss, actor.trainable_variables
    )

    critic_grad = ct.gradient(
        critic_loss, critic.trainable_variables
    )

    actor_optimizer.apply_gradients(
        zip(actor_grad, actor.trainable_variables)
    )

    critic_optimizer.apply_gradients(
        zip(critic_grad, critic.trainable_variables)
    )

    if episode % 10 == 0:
        print("Episode:", episode,
              "Reward:", reward)
