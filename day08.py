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

antinodes = set()
antinodesPart2 = set()

for key, values in charactersCoordinates.items() : 

    antenaPairs = list(combinations(values, 2))

    for pair in antenaPairs : 

        diffX = abs(pair[1][0] - pair[0][0])
        diffY = abs(pair[1][1] - pair[0][1])

        # A .
        # . A
        if pair[0][1] < pair[1][1] : 

            nwAntiNodeX = pair[0][0] - diffX
            nwAntiNodeY = pair[0][1] - diffY

            seAntiNodeX = pair[1][0] + diffX
            seAntiNodeY = pair[1][1] + diffY

            if antiNodeWithinLimits(nwAntiNodeX, nwAntiNodeY, maximumX, maximumY) : 
                antinodes.add(str(nwAntiNodeX) + "|" + str(nwAntiNodeY))
                # grid[nwAntiNodeX][nwAntiNodeY] = "#"

            if antiNodeWithinLimits(seAntiNodeX, seAntiNodeY, maximumX, maximumY) : 
                antinodes.add(str(seAntiNodeX) + "|" + str(seAntiNodeY))
                # grid[seAntiNodeX][seAntiNodeY] = "#"

            while antiNodeWithinLimits(nwAntiNodeX, nwAntiNodeY, maximumX, maximumY) : 
                antinodesPart2.add(str(nwAntiNodeX) + "|" + str(nwAntiNodeY))
                grid[nwAntiNodeX][nwAntiNodeY] = "#"

                nwAntiNodeX = nwAntiNodeX - diffX
                nwAntiNodeY = nwAntiNodeY - diffY

            while antiNodeWithinLimits(seAntiNodeX, seAntiNodeY, maximumX, maximumY) : 
                antinodesPart2.add(str(seAntiNodeX) + "|" + str(seAntiNodeY))
                grid[seAntiNodeX][seAntiNodeY] = "#"

                seAntiNodeX = seAntiNodeX + diffX
                seAntiNodeY = seAntiNodeY + diffY
        
        else : 
            # . A
            # A .

            neAntiNodeX = pair[0][0] - diffX
            neAntiNodeY = pair[0][1] + diffY

            swAntiNodeX = pair[1][0] + diffX
            swAntiNodeY = pair[1][1] - diffY

            if antiNodeWithinLimits(neAntiNodeX, neAntiNodeY, maximumX, maximumY) : 
                antinodes.add(str(neAntiNodeX) + "|" + str(neAntiNodeY))
                grid[neAntiNodeX][neAntiNodeY] = "#"

            if antiNodeWithinLimits(swAntiNodeX, swAntiNodeY, maximumX, maximumY) : 
                antinodes.add(str(swAntiNodeX) + "|" + str(swAntiNodeY))
                grid[swAntiNodeX][swAntiNodeY] = "#"

            while antiNodeWithinLimits(neAntiNodeX, neAntiNodeY, maximumX, maximumY) : 
                antinodesPart2.add(str(neAntiNodeX) + "|" + str(neAntiNodeY))
                grid[neAntiNodeX][neAntiNodeY] = "#"

                neAntiNodeX = neAntiNodeX - diffX
                neAntiNodeY = neAntiNodeY + diffY

            while antiNodeWithinLimits(swAntiNodeX, swAntiNodeY, maximumX, maximumY) : 
                antinodesPart2.add(str(swAntiNodeX) + "|" + str(swAntiNodeY))
                grid[swAntiNodeX][swAntiNodeY] = "#"

                swAntiNodeX = swAntiNodeX + diffX
                swAntiNodeY = swAntiNodeY - diffY

antenaAntinodes = 0 
for index in range(len(grid)) : 
    for j in range(len(grid[index])) : 
        if charactersCoordinates.get(grid[index][j]) : 
            antenaAntinodes += 1

print("Part 1:", len(antinodes))
print("Part 2:", len(antinodesPart2) + antenaAntinodes)