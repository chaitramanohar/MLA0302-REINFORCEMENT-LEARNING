import random

prices = [100, 105, 103, 110, 108, 115]

profit = 0
holding = False
buy_price = 0

for price in prices:
    action = random.choice(["Buy", "Sell", "Hold"])

    if action == "Buy" and not holding:
        holding = True
        buy_price = price
        print("Buy at", price)

    elif action == "Sell" and holding:
        holding = False
        profit += price - buy_price
        print("Sell at", price)

    else:
        print("Hold")

print("Total Profit =", profit)
