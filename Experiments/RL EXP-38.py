import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

conditions = [1, 2, 3]

performance = []

# Initial controller parameter
parameter = 0.5

for condition in conditions:

    target = condition * 10

    errors = []

    for step in range(50):

        output = parameter * target

        error = target - output

        # Adapt parameter based on feedback
        parameter += 0.01 * error

        errors.append(abs(error))

    performance.append(np.mean(errors))

    print(
        "Condition:", condition,
        "Final Parameter:",
        round(parameter, 3),
        "Average Error:",
        round(np.mean(errors), 3)
    )

plt.plot(conditions, performance, marker="o")

plt.xlabel("Operating Condition")
plt.ylabel("Average Error")
plt.title("Meta-Learning Adaptive Control")
plt.grid()
plt.show()
