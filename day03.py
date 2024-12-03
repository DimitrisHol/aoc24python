import re

with open("input/day03.txt", "r") as sourceFile : 

    total = 0 

    for line in sourceFile : 
        line = line.strip()

        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

        matches = re.findall(pattern, line)

        for x, y in matches : 

            total += int(x) * int(y)

    print(total)


        