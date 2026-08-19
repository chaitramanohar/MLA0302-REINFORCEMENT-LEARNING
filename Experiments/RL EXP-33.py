import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(10)

days = 200

# Simulated historical returns
stock = np.random.normal(0.001, 0.02, days)
bond = np.random.normal(0.0005, 0.008, days)
gold = np.random.normal(0.0007, 0.012, days)

returns = np.column_stack((stock, bond, gold))

# Portfolio strategies
portfolios = {
    "Aggressive": [0.7, 0.2, 0.1],
    "Balanced": [0.4, 0.4, 0.2],
    "Conservative": [0.2, 0.6, 0.2]
}

for name, weights in portfolios.items():

    portfolio_return = returns @ weights

    X = np.arange(days).reshape(-1, 1)
    y = np.cumsum(portfolio_return)

    model = LinearRegression()
    model.fit(X, y)

    predicted = model.predict(X)

    print(name)
    print("Final predicted value:",
          round(predicted[-1], 3))
    print()

    plt.plot(predicted, label=name)

plt.title("Predicted Portfolio Performance")
plt.xlabel("Days")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid()
plt.show()
