import numpy as np

states=5
gamma=0.9

reward=[0,2,0,-2,5]

V=np.zeros(states)

for i in range(20):
    for s in range(states-1):
        V[s]=reward[s]+gamma*V[s+1]

print("State Values")
print(V)
