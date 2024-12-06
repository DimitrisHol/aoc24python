import copy
from collections import defaultdict

def nextGuardPositionOutOfBounds(nextX, nextY, maxX, maxY) : 
    return nextX < 0 or nextY < 0 or nextX > maxX or nextY > maxY

grid = []
visitGrid = []

rowNum = 0

# starting position
x = 0
y = 0

with open("input/day06.txt", "r") as sourceFile : 

    for line in sourceFile : 

        row = list(line.strip())

        grid.append(row)
        visitGrid.append([0]* len(row))

        if "^" in row : 
            x = rowNum
            y = row.index("^")

            visitGrid[x][y] = True # this was the missing link ;) 

        rowNum +=1

gridCopy = copy.deepcopy(grid)

currentX = x
currentY = y

facing = ["N", "E", "S", "W"]
facingIndex = 0

visitCoords = []

while True : 

    direction = facing[facingIndex]

    nextPositionX = currentX
    nextPositionY = currentY

    if direction == "N" :
        nextPositionX += -1

    elif direction == "E" :
        nextPositionY += 1
    
    elif direction == "S" : 
        nextPositionX += 1
    
    elif direction == "W" :
        nextPositionY += -1

    if (nextGuardPositionOutOfBounds(nextPositionX, nextPositionY, len(grid) -1, len(row) -1)) : 
        break

    if grid[nextPositionX][nextPositionY] == "." :

        grid[currentX][currentY] = "."

        currentX = nextPositionX
        currentY = nextPositionY

        grid[currentX][currentY] = "^"

        # avoid duplicates
        if visitGrid[currentX][currentY] == False : 
            coords = [currentX, currentY]
            visitCoords.append(coords)

        visitGrid[currentX][currentY] = True

    elif grid[nextPositionX][nextPositionY] == "#" :
        facingIndex = (facingIndex + 1) %4

positionsReached = sum(x.count(True) for x in visitGrid)
print("escaped part 1 in ", positionsReached) 


# part 2: infinite loops : 
# Reset position
currentX = x
currentY = y

# Remove starting position
visitGrid[x][y] = False
obstacleLocationCount = 0 
print("checking", len(visitCoords), "possible points to obstruct")
for coords in visitCoords : 

    newCopy = copy.deepcopy(gridCopy)
    currentX = x
    currentY = y

    obstacleX = coords[0]
    obstacleY = coords[1]

    newCopy[obstacleX][obstacleY] = "#"

    facing = ["N", "E", "S", "W"]
    facingIndex = 0

    passPerPoint = defaultdict(int)

    while True :

        direction = facing[facingIndex]

        nextPositionX = currentX
        nextPositionY = currentY

        if direction == "N" :
            nextPositionX += -1

        elif direction == "E" :
            nextPositionY += 1
        
        elif direction == "S" : 
            nextPositionX += 1
        
        elif direction == "W" :
            nextPositionY += -1

        if (nextGuardPositionOutOfBounds(nextPositionX, nextPositionY, len(newCopy) -1, len(row) -1)) : 
            break

        if newCopy[nextPositionX][nextPositionY] == "." :

            newCopy[currentX][currentY] = "."

            currentX = nextPositionX
            currentY = nextPositionY

            newCopy[currentX][currentY] = "^"
            passPerPoint[str(currentX) + "|" + str(currentY)] += 1

        elif newCopy[nextPositionX][nextPositionY] == "#" :
            facingIndex = (facingIndex + 1) %4

        if passPerPoint[str(currentX) + "|" + str(currentY)] > 5 : 
            # print("possible loop", obstacleX, obstacleY)
            obstacleLocationCount +=1 
            break

print(obstacleLocationCount)