def positionWithinBounds(x, y, maxX, maxY) : 
    return x >= 0 or y >= 0 or x <= maxX or y <= maxY

rowNum = 0
grid = []
visitGrid = []

# trailhead = positions starting at 0 
trailheads = []
trailends = []

with open("input/day10.txt", "r") as sourceFile : 

    for line in sourceFile : 

        row = [int(x) for x in list(line.strip())]

        grid.append(row)
        visitGrid.append([0]* len(row))

        headIndexes = [[rowNum, index] for index, value in enumerate(row) if value == 0]
        trailheads.extend(headIndexes)

        endIndexes = [[rowNum, index] for index, value in enumerate(row) if value == 9]
        trailends.extend(endIndexes)

        rowNum +=1
print(trailheads, len(trailheads))
print(trailends, len(trailends))

adjacenyList = {}

for i in range(rowNum) : 
    for j in range(len(row)) : 

        adjacentSquares = []

        if i - 1 >= 0 and grid[i-1][j] - grid[i][j]  == 1 : 
            adjacentSquares.append([i-1, j])
        
        if i + 1 <= rowNum -1 and grid[i+1][j] - grid[i][j]  == 1 : 
            adjacentSquares.append([i+1, j])

        if j - 1 >= 0 and grid[i][j-1] - grid[i][j]  == 1 : 
            adjacentSquares.append([i, j-1])

        if j + 1 <= len(row) -1 and grid[i][j+1] - grid[i][j]  == 1 : 
            adjacentSquares.append([i, j+1])

        key = str(i) + "|" + str(j)

        adjacenyList[key] = adjacentSquares

winner = 0

for start in trailheads : 

    visited = set()
    stack = [start]

    while stack : 
        node = stack.pop()

        key = str(node[0]) + "|" + str(node[1])

        # add this for part 1 
        # if key not in visited : 

            # visited.add(key)

        if node in trailends : 
            winner += 1

        for neighbour in reversed(adjacenyList[key]) : 
            stack.append(neighbour)

print("winners :" , winner)