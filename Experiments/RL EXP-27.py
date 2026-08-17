import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

actor = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(3,)),
    layers.Dense(3, activation="softmax")
])

critic = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(3,)),
    layers.Dense(1)
])

actor_optimizer = tf.keras.optimizers.Adam(0.001)
critic_optimizer = tf.keras.optimizers.Adam(0.001)

for episode in range(100):

    state = np.random.rand(3).astype(np.float32)

    with tf.GradientTape() as actor_tape, \
         tf.GradientTape() as critic_tape:

        action_prob = actor(state.reshape(1, -1))
        value = critic(state.reshape(1, -1))

        action = tf.random.categorical(
            tf.math.log(action_prob), 1
        )[0, 0]

        reward = np.random.randn()

        advantage = reward - value[0, 0]

        actor_loss = -tf.math.log(
            action_prob[0, action]
        ) * advantage

        critic_loss = tf.square(advantage)

    actor_grads = actor_tape.gradient(
        actor_loss, actor.trainable_variables
    )

    critic_grads = critic_tape.gradient(
        critic_loss, critic.trainable_variables
    )

    actor_optimizer.apply_gradients(
        zip(actor_grads, actor.trainable_variables)
    )

    critic_optimizer.apply_gradients(
        zip(critic_grads, critic.trainable_variables)
    )

    if episode % 10 == 0:
        print("Episode:", episode,
              "Reward:", round(float(reward), 3))
