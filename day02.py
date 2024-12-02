def isGradual(levels) : 
     
     # must be either ascending or descending
     # change must be between 1, 2, or 3.

     ascending = levels.copy()
     descending = levels.copy()
     
     descending.sort()
     ascending.sort(reverse = True)

    #  print(levels, ascending, descending)

     if levels == ascending or levels == descending : 
        
        for i in range(len(levels) -1 ) : 
            diff = abs(int(levels[i]) - int(levels[i+1]))

            if diff > 3 or diff < 1: 
                return False
        
        return True

     else : 
         return False

with open("input/day02.txt", "r") as sourceFile : 

    safeCounter = 0

    for line in sourceFile : 
        line = line.strip()

        levels = [int(x) for x in line.split(" ")]

        print(levels, isGradual(levels))

        if (isGradual(levels)) : 
            safeCounter += 1

    print(safeCounter)