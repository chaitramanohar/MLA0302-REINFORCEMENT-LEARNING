import random

reward=[]

for i in range(100):

    reward.append(random.randint(1,10))

print("Average Reward")

print(sum(reward)/len(reward))
