def ascOrDesc(levels) : 

    ascending = levels.copy()
    descending = levels.copy()
    
    descending.sort()
    ascending.sort(reverse = True)

    return levels == ascending or levels == descending

def validDIff(levels) : 

    for i in range(len(levels) -1 ) : 
        diff = abs(int(levels[i]) - int(levels[i+1]))

        if diff > 3 or diff < 1: 
            return False
        
    return True

def isGradualPart1(levels) : 
     
    if ascOrDesc(levels) and validDIff(levels) : 
        return True

def isGradualPart2(levels) :  

    if ascOrDesc(levels) and validDIff(levels) : 
        return True
    else : 

        for i in range(len(levels)) : 

            levelCopy = levels.copy()
            levelCopy.pop(i)

            if ascOrDesc(levelCopy) and validDIff(levelCopy) : 
                return True
        else : 
            return False
        
with open("input/day02.txt", "r") as sourceFile : 

    safePart1 = 0
    safePart2 = 0

    for line in sourceFile : 
        line = line.strip()

        levels = [int(x) for x in line.split(" ")]

        if (isGradualPart1(levels)) : 
            safePart1 += 1

        if (isGradualPart2(levels)) : 
            safePart2 += 1

    print(safePart1)
    print(safePart2)