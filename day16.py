import heapq
from collections import defaultdict

def dijkstra(startPosition, endPosition, maxCost) : 

    # 0 = N
    # 1 = E 
    # 2 = S
    # 3 = W

    nextCoordinates = { 
        0 : (-1,  0),
        1 : ( 0,  1),
        2 : ( 1,  0),
        3 : ( 0, -1)
    }

    # We don't need adjacency list, since we are moving forward
    # new nodes can only be ahead

    distance = defaultdict(lambda: 100000)

    # startX, startY, 1 = EAST
    distance[startPosition] = 0

    visited = set() 

    # x, y, direction, tentative cost
    priorityQueue = []
    heapq.heappush(priorityQueue, (startPosition[0], startPosition[1], startPosition[2], 0))

    while priorityQueue : 

        x, y, direction, cost = heapq.heappop(priorityQueue)

        if (x, y) == endPosition : 
            # print("Part 1 :", cost, "direction", direction)
            return cost, distance

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

    return -1, []

with open("input/test/day16.txt", "r") as sourceFile : 

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
part1Result, distanceTable = dijkstra(startPosition, endPosition, None)
print("Part 1 : ", part1Result)


# Part 2 : 
# Nodes are part of the shortest path if for (x, y, direction)
# distance(start - node) + distance(node - end) = shortest distance

# The first part we already have from the `distance` dictionary
# The second part, can essentially be again a dijkstra from the end this time 
# each of the valid nodes. 
# we can trim the number of nodes, by checking if the distance from start to the node (already computed)
# is already bigger than the shortest path we want to reach. (Trimming further away nodes)

shortestPathDistance = part1Result

# Shortest path
validOptions = set() 
for node, distanceCost in distanceTable.items() : 

    # doesn't make sense to continue if already too far away
    if distanceCost >= shortestPathDistance : 
        continue

    # Re-run shortest path to the end.
    distanceToEnd, _ = dijkstra(node, endPosition, shortestPathDistance)
    if distanceToEnd == -1 : 
        continue

    if distanceCost + distanceToEnd == shortestPathDistance : 
        validOptions.add((node[0], node[1]))

# Also add the final position ;) 
validOptions.add((endPosition[0], endPosition[1]))

print("Part 2 :", len(validOptions))