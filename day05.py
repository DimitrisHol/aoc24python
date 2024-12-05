with open("input/day05.txt", "r") as sourceFile : 

    # Used for parsing 
    midpointPassed = False

    rules = []

    resultPart1 = 0
    resultPart2 = 0

    for line in sourceFile : 
        line = line.strip()

        if line == "" : 
            midpointPassed = True
            continue

        if (not midpointPassed) : 

            rule = line.split("|")
            rules.append(rule)

        else : 
            update = line.split(",")

            # part 1
            updateIsValid = True
            for rule in rules : 

                if (not updateIsValid) : 
                    break

                try : 
                    indexPageA = update.index(rule[0])
                    indexPageB = update.index(rule[1])

                    if (indexPageA > indexPageB) : 
                        updateIsValid = False

                except ValueError : 
                    continue # no match found
            
            if updateIsValid :
                resultPart1 += int(update[len(update) // 2])

            # part 2 : 
            relevantRules = []
            updateToBeFixed = False
            for rule in rules : 

                try : 
                    indexPageA = update.index(rule[0])
                    indexPageB = update.index(rule[1])

                    relevantRules.append(rule)
                    if (indexPageA > indexPageB) : 
                        updateToBeFixed = True

                except ValueError : 
                    continue # no match found

            if updateToBeFixed : 

                # winner of most 1v1 is first
                wins = {page: 0 for page in update}
                for rule in relevantRules : 
                    wins[rule[0]] += 1

                winsSortedDesc = sorted(wins, key=wins.get, reverse=True)
                resultPart2 += int(winsSortedDesc[len(winsSortedDesc) // 2])

print(resultPart1)
print(resultPart2)