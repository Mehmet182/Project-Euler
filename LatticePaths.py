'''

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

a diagram of 6 2 by 2 grids showing all the routes to the bottom right corner
How many such routes are there through a given gridSize?

'''

def latticePaths(gridSize):
    for i in range(len(gridSize)):
        for j in (len(gridSize)):
            