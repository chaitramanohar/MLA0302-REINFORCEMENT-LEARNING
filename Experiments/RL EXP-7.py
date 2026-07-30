gamma=0.9

reward=[1,1,1,10]

V=[0,0,0,0]

for i in range(10):

    for s in range(3):

        V[s]=reward[s]+gamma*V[s+1]

print(V)
