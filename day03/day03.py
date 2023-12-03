def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    """
    iterate through each index to find all indicies that I should check if it has a number
    now, iterate thorugh digits again and get each number
    check if the number is in the set of indicies that I should check
    if so, add the number
    """
    total = 0
    char2DList = [[char for char in string] for string in lines]
    symbolIndices = set()
    checkIndices = set()
    for i in range(len(char2DList)):
        for j in range(len(char2DList[i])):
            if char2DList[i][j] != '.' and not char2DList[i][j].isdigit():
                symbolIndices.add((i, j))

    for index in symbolIndices:
        for i in range(-1, 2):
            for j in range(-1, 2):
                checkIndices.add((index[0] + i, index[1] + j))
    
    currNum = ""
    currNumCheck = False
    for i in range(len(char2DList)):
        for j in range(len(char2DList[i])):
            if char2DList[i][j].isdigit():
                currNum += char2DList[i][j]
                if (i, j) in checkIndices:
                    currNumCheck = True
            else:
                if currNumCheck:
                    total += int(currNum)
                currNum = ""
                currNumCheck = False
    return total


def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    """
    store * index map to index -> neighboring numbers
    parse through numbers and check if neighboring to *. if so, add number to index key
    iterate through keys to check which ones only have 2 and multiply
    """
    total = 0
    indexMap = {}
    char2DList = [[char for char in string] for string in lines]
    for i in range(len(char2DList)):
        for j in range(len(char2DList[i])):
            if char2DList[i][j] == '*':
                indexMap[(i, j)] = []

    currNum = ""
    currNumNeighboringGear = set()
    for i in range(len(char2DList)):
        for j in range(len(char2DList[i])):
            if char2DList[i][j].isdigit():
                currNum += char2DList[i][j]
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (i + x, j + y) in indexMap: currNumNeighboringGear.add((i + x, j + y))
            else:
                if currNum != "":
                    if len(currNumNeighboringGear) > 1:
                        print("Panic, there's more than one neighboring gear")
                        return
                    elif len(currNumNeighboringGear) == 1:
                        gearIndex = currNumNeighboringGear.pop()
                        indexMap[gearIndex].append(int(currNum))
                currNum = ""
                currNumNeighboringGear = set()

    for index in indexMap:
        if len(indexMap[index]) == 2:
            total += indexMap[index][0] * indexMap[index][1]
    return total
                

if __name__ == "__main__":
    input_path = "./day03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))