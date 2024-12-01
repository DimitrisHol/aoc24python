with open("input/day01.txt", "r") as sourceFile : 

    locAList = []
    locBList = []

    for line in sourceFile : 
        line = line.strip()
        content = line.split("   ")

        locationA = int(content[0])
        locationB = int(content[1])

        locAList.append(locationA)
        locBList.append(locationB)

locAList.sort()
locBList.sort()

diffSum = 0
similarityScore = 0

for index in range(len(locAList)) : 

    # Part 1 
    diff = abs(locAList[index] - locBList[index])
    diffSum += diff

    # Part 2 : 
    value = locAList[index] * locBList.count(locAList[index])
    similarityScore += value

print(diffSum)
print(similarityScore)
