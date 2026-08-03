import numpy as np

epsilon = 0.2

Q = [10, 15, 20]

for i in range(20):

    if np.random.rand() < epsilon:

        action = np.random.randint(3)

        print("Exploration -> Action", action)

    else:

        action = np.argmax(Q)

        print("Exploitation -> Action", action)
