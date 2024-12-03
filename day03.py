import re


with open("input/day03.txt", "r") as sourceFile : 

    totalPart1 = 0 
    totalPart2 = 0 
    multiply = True

    for line in sourceFile : 
        line = line.strip()

        pattern = r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))'

        matches = re.findall(pattern, line)

        for x in matches : 

            if x == "don\'t()" : 
                multiply = False
            elif x == "do()" : 
                multiply = True
            else : 
                value = [int(y) for y in x[4:len(x) -1].split(",")]
                totalPart1 += value[0] * value[1]
                if multiply : 
                    totalPart2 += value[0] * value[1]

    print(totalPart1)
    print(totalPart2)