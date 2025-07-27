def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        seedString, mapList = lines[0], lines[2:]
        seeds = [int(num) for num in seedString.split(":")[1].strip().split(" ")]
        currMaps = []
        for mapLine in mapList:
            splitMap = mapLine.split(" ")
            if len(splitMap) == 3:
                destIndex, startIndex, length = int(splitMap[0]), int(splitMap[1]), int(splitMap[2])
                currMaps.append((destIndex, startIndex, length))
            elif len(splitMap) == 2:
                newSeeds = []
                for i, seed in enumerate(seeds):
                    for currMap in currMaps:
                        if seed - currMap[1] < currMap[2] and seed - currMap[1] >= 0:
                            newSeeds.append(seed - currMap[1] + currMap[0])
                            break
                    if len(newSeeds) <= i:
                        newSeeds.append(seed)
                seeds = newSeeds
                currMaps = []
        newSeeds = []
        for i, seed in enumerate(seeds):
            for currMap in currMaps:
                if seed - currMap[1] < currMap[2] and seed - currMap[1] >= 0:
                    newSeeds.append(seed - currMap[1] + currMap[0])
                    break
            if len(newSeeds) <= i:
                newSeeds.append(seed)
        seeds = newSeeds
        currMaps = []
        return min(seeds)

def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        seedString, mapList = lines[0], lines[3:]
        seeds = [int(num) for num in seedString.split(":")[1].strip().split(" ")]
        seedPairs = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0,len(seeds),2)]
        allSeedMaps = []

        currMaps = []
        for mapLine in mapList:
            splitMap = mapLine.split(" ")
            if len(splitMap) == 3:
                destIndex, startIndex, length = int(splitMap[0]), int(splitMap[1]), int(splitMap[2])
                currMaps.append((destIndex, startIndex, length))
            elif len(splitMap) == 2:
                allSeedMaps.append(currMaps)
                currMaps = []
        allSeedMaps.append(currMaps)
        
        currResult = 0
        while True:
            potentialSeed = currResult
            for seedMaps in allSeedMaps[::-1]:
                for seedMap in seedMaps[::-1]:
                    if seedMap[0] <= potentialSeed < seedMap[0] + seedMap[2]:
                        potentialSeed = potentialSeed - seedMap[0] + seedMap[1]
                        break
            for seedPair in seedPairs:
                if seedPair[0] <= potentialSeed < seedPair[1]:
                    return currResult
            currResult += 1

if __name__ == "__main__":
    input_path = "./day05/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))