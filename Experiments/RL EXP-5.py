gamma=0.9

V=[0,0,0,5]

for i in range(10):

    for s in range(3):

        V[s]=1+gamma*V[s+1]

print(V)
