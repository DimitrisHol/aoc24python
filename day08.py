from collections import defaultdict
from itertools import combinations

def antiNodeWithinLimits(x, y, maxX, maxY) : 

    return x >= 0 and y >= 0 and x <= maxX-1 and y <= maxY-1 


with open("input/day08.txt", "r") as sourceFile : 

    grid = []
    charactersCoordinates = defaultdict(list)

    rowNum = 0 
    for line in sourceFile : 

        row = list(line.strip())

        grid.append(row)

        for index in range(len(row)) : 

            if (row[index] != ".") : 
                coordinates = [rowNum, index]
                charactersCoordinates[row[index]].append(coordinates)
        rowNum += 1 

maximumX = len(grid)
maximumY = len(row)

print(maximumX, maximumY)

antinodes = set()

# for row in grid : 
#     print(row)
        
for key, values in charactersCoordinates.items() : 

    # if key == "A" : 
        # continue

    antenaPairs = list(combinations(values, 2))

    for pair in antenaPairs : 

        diffX = abs(pair[1][0] - pair[0][0])
        diffY = abs(pair[1][1] - pair[0][1])

        if diffX <= 0 or diffY <= 0 : 
            print("WHAT THE FUCK ")
            exit(1)
        
        # print(pair[0], pair[1], "diff[", diffX, diffY, "]")

        nwAntiNodeX = pair[0][0] - diffX
        nwAntiNodeY = pair[0][1] - diffY

        seAntiNodeX = pair[1][0] + diffX
        seAntiNodeY = pair[1][1] + diffY

        # print("possible anti-node 1: ", nwAntiNodeX, nwAntiNodeY)
        # print("possible anti-node 2: ", seAntiNodeX, seAntiNodeY)

        if antiNodeWithinLimits(nwAntiNodeX, nwAntiNodeY, maximumX, maximumY) : 
            antinodes.add(str(nwAntiNodeX) + "|" + str(nwAntiNodeY))
            grid[nwAntiNodeX][nwAntiNodeY] = "#"

        if antiNodeWithinLimits(seAntiNodeX, seAntiNodeY, maximumX, maximumY) : 
            antinodes.add(str(seAntiNodeX) + "|" + str(seAntiNodeY))
            grid[seAntiNodeX][seAntiNodeY] = "#"


print(antinodes, len(antinodes))

# for row in grid : 
#     print(row)
        
# 470 too high

# let's try the experimental transposed