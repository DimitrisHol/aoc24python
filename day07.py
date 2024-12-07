from itertools import product

with open("input/day07.txt", "r") as sourceFile : 

    operators = ["+", "*"]
    operatorsPart2 = ["+", "*", "||"]

    targetReachedTotal = 0
    targetReachedTotalPart2 = 0

    for line in sourceFile : 

        row = line.strip().split(": ")

        target = int(row[0])
        numbers = row[1].split(" ")

        # spots = numbers - 1
        operatorSpots = len(numbers) - 1 

        # part 1 :

        # total combinations = 2 ^ spots
        combinations = product(operators, repeat=operatorSpots)

        result = 0

        for comb in combinations : 

            result = int(numbers[0])
            for index in range(len(comb)) : 

                if comb[index] == "+" : 
                    result += int(numbers[index +1])
                else : 
                    result *= int(numbers[index +1])

            if target == result : 
                targetReachedTotal += target
                break

        # part 2 : 
        combinations = product(operatorsPart2, repeat=operatorSpots)

        result = 0

        for comb in combinations : 

            result = int(numbers[0])
            for index in range(len(comb)) : 

                if comb[index] == "+" : 
                    result += int(numbers[index +1])
                elif comb[index] == "*" : 
                    result *= int(numbers[index +1])
                else : 
                    result = int(str(result) + numbers[index +1])

            if target == result : 
                targetReachedTotalPart2 += target
                break

print(targetReachedTotal)
print(targetReachedTotalPart2)