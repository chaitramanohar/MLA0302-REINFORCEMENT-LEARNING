import random

returns=[]

for episode in range(20):

    reward=random.randint(5,15)

    returns.append(reward)

print("Average Return")

print(sum(returns)/len(returns))
