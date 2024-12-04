import re

with open("input/day04.txt", "r") as sourceFile : 

    data = []

    for line in sourceFile : 
        line = line.strip()

        row = []
        for char in line : 
            row.append(char)
        data.append(row.copy())

totalTimes = 0

pattern = r'XMAS'

# horizontal
for row in data : 

    totalTimes += len(re.findall(pattern, "".join(row)))
    totalTimes += len(re.findall(pattern, "".join(row[::-1])))

# vertical
for j in range(len(data[0])) : 

    column = [data[i][j] for i in range(len(data))]

    totalTimes += len(re.findall(pattern, "".join(column)))
    totalTimes += len(re.findall(pattern, "".join(column[::-1])))

# diagonal
for i in range(len(data) - 3) :
    for j in range(len(data[0]) -3) : 
        miniTable = []

        for x in range(4) : 
            row = []
            for y in range(4) : 
                row.append(data[i+x][j+y])
            miniTable.append(row)

        main_diagonal = [miniTable[k][k] for k in range(4)]
        anti_diagonal = [miniTable[k][3-k] for k in range(4)]

        totalTimes += len(re.findall(pattern, "".join(main_diagonal)))
        totalTimes += len(re.findall(pattern, "".join(main_diagonal[::-1])))

        totalTimes += len(re.findall(pattern, "".join(anti_diagonal)))
        totalTimes += len(re.findall(pattern, "".join(anti_diagonal[::-1])))


# part 2 : 
totalTimesPart2 = 0

for i in range(len(data) - 2) :
    for j in range(len(data[0]) -2) : 
        miniTable = []

        for x in range(3) : 
            row = []
            for y in range(3) : 
                row.append(data[i+x][j+y])
            miniTable.append(row)

        main_diagonal = [miniTable[k][k] for k in range(3)]
        anti_diagonal = [miniTable[k][2-k] for k in range(3)]

        mainDString = "".join(main_diagonal)
        antiDString = "".join(anti_diagonal)

        if (mainDString in ["MAS", "SAM"] and antiDString in ["MAS", "SAM"]) : 
            totalTimesPart2 += 1
        
print(totalTimes)
print(totalTimesPart2)