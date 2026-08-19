import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(5)

days = 100

price = np.random.uniform(10, 30, days)

# Demand decreases as price increases
demand = 100 - 2.5 * price + np.random.normal(0, 5, days)

# Train predictive demand model
X = price.reshape(-1, 1)
y = demand

model = LinearRegression()
model.fit(X, y)

prices = np.arange(5, 41)

predicted_demand = model.predict(
    prices.reshape(-1, 1)
)

revenue = prices * predicted_demand

best_index = np.argmax(revenue)

best_price = prices[best_index]

print("Optimal Price:", best_price)
print("Expected Demand:",
      round(predicted_demand[best_index], 2))
print("Expected Revenue:",
      round(revenue[best_index], 2))

plt.plot(prices, revenue)
plt.scatter(best_price, revenue[best_index],
            color="red")

plt.xlabel("Price")
plt.ylabel("Expected Revenue")
plt.title("Dynamic Pricing Optimization")
plt.grid()
plt.show()
