# 0 = N
# 1 = E 
# 2 = S
# 3 = W

from collections import defaultdict

with open("input/day16.txt", "r") as sourceFile : 

    grid = []

    rowNum = 0 
    for line in sourceFile : 

        row = list(line.strip())
        grid.append(row)

        for index in range(len(row)) : 

            if row[index] == "S" : 
                startPosition = (rowNum, index, 1)
            elif row[index] == "E" : 
                endPosition = (rowNum, index)

        rowNum += 1 

print("Start", startPosition, "End",  endPosition)

# We don't need adjacency list, since we are moving forward
# new nodes can only be ahead

nextCoordinates = { 
    0 : (-1,  0),
    1 : ( 0,  1),
    2 : ( 1,  0),
    3 : ( 0, -1)
}

distance = defaultdict(lambda: 100000)

# startX, startY, 1 = EAST
distance[startPosition] = 0

visited = set() 

# x, y, direction, tentative cost
priorityQueue = [(startPosition[0], startPosition[1], startPosition[2], 0)]

while priorityQueue : 

    x, y, direction, cost = priorityQueue.pop(0)

    if (x, y) == endPosition : 
        print("Part 1 :", cost, "direction", direction)
        break

    if (x, y, direction) in visited : 
        continue
    else : 
        visited.add((x, y, direction))

    # Check the one in front 
    coordinateDiff = nextCoordinates[direction]

    newX = x + coordinateDiff[0]
    newY = y + coordinateDiff[1]

    if grid[newX][newY] != "#" : 

        # moved forward
        newCost = cost + 1
        if newCost < distance[(newX, newY, direction)] : 
            distance[(newX, newY, direction)] = newCost
            priorityQueue.append((newX, newY, direction, newCost))

    # Check two sides    
    newDirections = [(direction - 1) % 4, (direction + 1) % 4]

    # only turn, not move ! 
    for newDirection in newDirections : 

        newCost = cost + 1000
        if newCost < distance[(x, y, newDirection)] : 
            distance[(x, y, newDirection)] = newCost
            priorityQueue.append((x, y, newDirection, newCost))

    # We need to sort the priority queue
    priorityQueue.sort(key = lambda x: x[3])