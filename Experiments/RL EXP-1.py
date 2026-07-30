import numpy as np

grid = np.zeros((5,5))

dirt = [(1,2),(2,4),(4,1)]
obstacles = [(1,1),(3,3)]

for d in dirt:
    grid[d]=1

for o in obstacles:
    grid[o]=-1

robot=(0,0)

print("Grid World")
print(grid)

moves=[(0,1),(1,0),(0,-1),(-1,0)]

for move in moves:
    x=robot[0]+move[0]
    y=robot[1]+move[1]

    if 0<=x<5 and 0<=y<5:
        print("Robot moved to",(x,y))
