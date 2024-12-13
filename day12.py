from collections import defaultdict

def positionWithinBounds(x, y, maxX, maxY) : 
    return x >= 0 and y >= 0 and x <= maxX -1 and y <= maxY -1


def count_teeth_from_indices(indices):
    if not indices:
        return 0
    
    count = 0
    clusters = []
    current_cluster = [indices[0]]

    # Step 1: Group consecutive indices into clusters
    for i in range(1, len(indices)):
        if indices[i] == indices[i - 1] + 1:  # If it's consecutive
            current_cluster.append(indices[i])
        else:
            clusters.append(current_cluster)
            current_cluster = [indices[i]]
    clusters.append(current_cluster)  # Add the last cluster
    
    # Step 2: Count the teeth by checking the isolation of each cluster
    for cluster in clusters:
        left_gap = cluster[0] == 0 or (cluster[0] - 1) not in indices  # Left edge is clear
        right_gap = (cluster[-1] + 1) not in indices  # Right edge is clear
        if left_gap or right_gap:
            count += 1
            
    return count

rowNum = 0
grid = []

with open("input/day12.txt", "r") as sourceFile : 

    for line in sourceFile : 

        row = [character for character in line.strip()]

        grid.append(row)

        rowNum +=1

adjacenyList = {}

for i in range(rowNum) : 
    for j in range(len(row)) : 

        adjacentSquares = []

        if i - 1 >= 0 and grid[i-1][j] == grid[i][j] : 
            adjacentSquares.append([i-1, j])
        
        if i + 1 <= rowNum -1 and grid[i+1][j] == grid[i][j] : 
            adjacentSquares.append([i+1, j])

        if j - 1 >= 0 and grid[i][j-1] == grid[i][j] : 
            adjacentSquares.append([i, j-1])

        if j + 1 <= len(row) -1 and grid[i][j+1] == grid[i][j] : 
            adjacentSquares.append([i, j+1])

        key = str(i) + "|" + str(j)

        adjacenyList[key] = adjacentSquares

# DFS for group of regions : 
regionID = 0 
regionMap = defaultdict(list)
regionCount = defaultdict(int)

visited = set()

for key in adjacenyList.keys() : 

    if key in visited : 
        continue

    # We are in new group
    regionID += 1

    # Starting node
    x = key.split("|")[0]
    y = key.split("|")[1]

    groupCoordinates = set()

    stack = [[x,y]]

    while stack : 

        node = stack.pop()
        nodeKey = str(node[0]) + "|" + str(node[1])

        if nodeKey in groupCoordinates : 
            continue

        visited.add(nodeKey)
        grid[int(node[0])][int(node[1])] = regionID
        groupCoordinates.add(nodeKey)

        for neighbour in adjacenyList[nodeKey] : 
            stack.append(neighbour)

    regionMap[regionID] = list(groupCoordinates)    

perimeterCount = defaultdict(int)

neighbours = [(-1, 0), (0 , 1), (1, 0), (0, -1)]

for x in range(len(grid)) : 

    for y in range(len(grid[x])) : 

        region = grid[x][y]
        regionCount[region] += 1

        for n in neighbours : 

            nPositionX = x + n[0]
            nPositionY = y + n[1]

            if positionWithinBounds(nPositionX, nPositionY, rowNum, len(grid[x])) : 

                if grid[nPositionX][nPositionY] != region : 
                    # neighbour is different, then fence
                    
                    perimeterCount[region] += 1
            else : 
                # edge of grid, fence
                perimeterCount[region] += 1

regionMapPerimeter = defaultdict(int)

for regionId, regions in regionMap.items() : 

    # print("ID : ", regionId)

    xValues = [int(item.split('|')[0]) for item in regions]
    yValues = [int(item.split('|')[1]) for item in regions]

    minX = min(xValues)
    maxX = max(xValues)

    minY = min(yValues)
    maxY = max(yValues)

    for i in range(minX, maxX + 1) : 

        currentRegions = [x for x in regions if int(x.split('|')[0]) == i]
        
        topBlocks = []
        botBlocks = []
        for region in currentRegions : 

            x = int(region.split("|")[0])
            y = int(region.split("|")[1])

            if x - 1 < 0 or grid[x-1][y] != regionId : 
                topBlocks.append(y)

            if x + 1 >= rowNum or grid[x+1][y] != regionId : 
                botBlocks.append(y)

        localSum = 0
        topBlocks.sort()
        if len(topBlocks) == 1 : 
            localSum = 1
        else : 
            localSum += count_teeth_from_indices(topBlocks)
        # print("top blocks sum :", localSum)
        regionMapPerimeter[regionId] += localSum

        localSum = 0
        botBlocks.sort()
        if len(botBlocks) == 1 : 
            localSum = 1
        else : 
            localSum += count_teeth_from_indices(botBlocks)
        # print("bot blocks sum :", localSum)
        regionMapPerimeter[regionId] += localSum

    for i in range(minY, maxY + 1) :

        currentRegions = [y for y in regions if int(y.split('|')[1]) == i]

        eastBlocks = []
        westBlocks = []

        for region in currentRegions : 

            x = int(region.split("|")[0])
            y = int(region.split("|")[1])

            if y + 1 >= len(row) or grid[x][y+1] != regionId : 
                eastBlocks.append(x)

            if y - 1 < 0 or grid[x][y-1] != regionId : 
                westBlocks.append(x)


        localSum = 0
        eastBlocks.sort()
        if len(eastBlocks) == 1 : 
            localSum = 1
        else : 
            localSum += count_teeth_from_indices(eastBlocks)
        # print("east blocks sum :", localSum)
        regionMapPerimeter[regionId] += localSum

        localSum = 0
        westBlocks.sort()
        if len(westBlocks) == 1 : 
            localSum = 1
        else : 
            localSum += count_teeth_from_indices(westBlocks)
        # print("west blocks sum :", localSum)
        regionMapPerimeter[regionId] += localSum
            
part1Result = 0 
part2Result = 0 

for key, perimeter in perimeterCount.items() : 

    # print(key, regionCount[key],"*" ,  perimeter, regionCount[key] * perimeter)
    part1Result += regionCount[key] * perimeter

for key, perimeter in regionMapPerimeter.items() : 

    # print("Key:", key," ||" ,regionCount[key],"*" ,  perimeter, regionCount[key] * perimeter)
    part2Result += regionCount[key] * regionMapPerimeter[key]


print("part 1:", part1Result)
print("part 2:", part2Result)