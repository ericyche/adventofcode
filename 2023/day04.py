def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        total = 0
        for line in lines:
            cards = line.split(":")[1]
            winningNumsString, haveNumsString = cards.split("|")
            winningNums = set(winningNumsString.strip().split())
            haveNums = set(haveNumsString.strip().split())
            total += int(2 ** (len(winningNums & haveNums) - 1))
        return total

def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        numScratchCards = [1] * len(lines)
        for i in range(len(lines)):
            line = lines[i]
            cards = line.split(":")[1]
            winningNumsString, haveNumsString = cards.split("|")
            winningNums = set(winningNumsString.strip().split())
            haveNums = set(haveNumsString.strip().split())
            for j in range(i + 1, i + 1 + len(winningNums & haveNums)):
                numScratchCards[j] += numScratchCards[i]
        return sum(numScratchCards)

if __name__ == "__main__":
    input_path = "./day04/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))