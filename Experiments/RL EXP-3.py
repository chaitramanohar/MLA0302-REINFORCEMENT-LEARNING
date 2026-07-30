import random

arms=[5,8,10]

for i in range(10):

    action=random.randint(0,2)

    reward=arms[action]

    print("Arm",action,"Reward",reward)
