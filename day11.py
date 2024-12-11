from collections import defaultdict

def numberOfDigits(number) :  

    for i in range(1, 20) : 
        if number // (10 ** i) == 0 : 
            return i

with open("input/day11.txt", "r") as sourceFile : 

    for line in sourceFile : 

        stones = [int(x) for x in line.strip("").split(" ")]

stoneCount = defaultdict(int)

for stone in stones : 
    stoneCount[stone] = 1

for blink in range(75) : 


    if blink == 25 : 
        part1 = 0 

        for stone in stoneCount.keys() : 
        
            part1 += stoneCount[stone]

        print("Part 1 :", part1)

    keys = stoneCount.copy()

    for key, frequency in keys.items() : 

        stoneCount[key] -= frequency
        if stoneCount[key] == 0 : 
            stoneCount.pop(key)

        if key == 0 : 
            
            stoneCount[1] += frequency
        
        elif numberOfDigits(key) % 2 == 0: 

            asString = str(key)

            leftPart = asString[:len(asString) // 2]
            rightPart = asString[len(asString) // 2:]

            stoneCount[int(leftPart)] += frequency
            stoneCount[int(rightPart)] += frequency

        else : 
            stoneCount[key * 2024] += frequency


part2 = 0 
for stone in stoneCount.keys() : 
    part2 += stoneCount[stone]

print("Part 2 :", part2)
