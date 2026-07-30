import random

ads=["A","B","C"]

clicks=[0,0,0]

for i in range(20):

    ad=random.randint(0,2)

    clicks[ad]+=1

print(clicks)
