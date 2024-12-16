from collections import defaultdict
import math

positionCounter = defaultdict(int)

with open("input/day14.txt", "r") as sourceFile : 

    maxX = 101
    maxY = 103

    for line in sourceFile : 

        line = line.strip().split(" ")

        position = line[0]
        x = int(position.split(",")[0].split("=")[1])
        y = int(position.split(",")[1])

        velocity = line[1]
        velocX = int(velocity.split(",")[0][2:])
        velocY = int(velocity.split(",")[1])

        currentPositionX = x
        currentPositionY = y
        for i in range(100) : 

            currentPositionX += velocX
            currentPositionY += velocY
            
        finalX = currentPositionX % maxX
        finalY = currentPositionY % maxY

        positionCounter[(finalX,finalY)] += 1

nwCounter = 0 
neCounter = 0 
seCounter = 0 
swCounter = 0 

for position, numberOfRobots in positionCounter.items() : 

    # grid[position[1]][position[0]] = numberOfRobots

    horizontalLimit = maxX // 2
    verticalLimit = maxY // 2

    if position[0] < horizontalLimit and position[1] < verticalLimit: 
        nwCounter += numberOfRobots
    elif position[0] < horizontalLimit and position[1] > verticalLimit: 
        neCounter += numberOfRobots
    elif position[0] > horizontalLimit and position[1] > verticalLimit: 
        seCounter += numberOfRobots
    elif position[0] > horizontalLimit and position[1] < verticalLimit: 
        swCounter += numberOfRobots


print("part1Answer", nwCounter * neCounter * seCounter * swCounter)

from PIL import Image

# Convert the grid to a BMP image
def grid_to_bmp(grid, filename):
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    print(height, width)
    
    # Create a new image with '1' mode (1-bit pixels, black and white)
    image = Image.new('1', (width, height))
    
    # Set pixel values based on the grid (1 = white, 0 = black)
    for y in range(height):
        for x in range(width):

            color = 255 if grid[y][x] == 1 else 0
            image.putpixel((x, y), color)  # (x, y) coordinates

    image.save(filename, 'BMP')  # Save the image as BMP

maxX = 101
maxY = 103

# Part 2: 
grid = []
for i in range (maxY) : 
    grid.append([0] * maxX)

# map : (index -> (position, velocity))
robotMap = {}

robotId = 0
with open("input/day14.txt", "r") as sourceFile : 

    for line in sourceFile : 

        line = line.strip().split(" ")

        position = line[0]
        x = int(position.split(",")[0].split("=")[1])
        y = int(position.split(",")[1])

        velocity = line[1]
        velocX = int(velocity.split(",")[0][2:])
        velocY = int(velocity.split(",")[1])

        robotMap[robotId] = ((x, y), (velocX, velocY))
        robotId += 1

for i in range(6600) : 

    grid = []
    for y in range (maxY) : 
        grid.append([0] * maxX)

    # loop through robots
    for rId , (position, velocity) in robotMap.items() : 

        # print(rId, position, velocity)

        currentX = (position[0] + (velocity[0] * i)) % maxX
        currentY = (position[1] + (velocity[1] * i)) % maxY

        grid[currentY][currentX] = 1

    filename = f'out/output_{i:04}.bmp'
    # grid_to_bmp(grid, filename)

print("part2Answer", 6512)