def safe_index(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1

row = []

with open("input/day09.txt", "r") as sourceFile : 

    for line in sourceFile : 

        row = list(line.strip())

blocks = []
counter = 0 

for i in range(len(row)) : 

    if i == 0 or i % 2 == 0 : 

        for i in range(int(row[i])) : 
            blocks.append(counter)
        counter += 1
        
    else : 
        for i in range(int(row[i])) : 
            blocks.append(".")

lastKnownDigitPos = len(blocks) -1

if safe_index(blocks, ".") != -1  : 

    while blocks.index(".") < lastKnownDigitPos : 

        indexToReplace = blocks.index(".")

        for i in (range(lastKnownDigitPos, 0, -1) ) : 

            if blocks[i] != "." : 
                lastKnownDigitPos = i
                break 

        # edge case
        if  blocks.index(".") >= lastKnownDigitPos : 
            break

        blocks[indexToReplace] = blocks[lastKnownDigitPos]
        blocks[lastKnownDigitPos] = "."
        
        lastKnownDigitPos -= 1
        # print(''.join(map(str, blocks)), blocks.index(".") , lastKnownDigitPos)

    blocks = blocks[:lastKnownDigitPos+1]
    # print(blocks)

checkSum = 0 

for index in range(len(blocks)) :
    checkSum += index * blocks[index]

print("part1 :", checkSum)
