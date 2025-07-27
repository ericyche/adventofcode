from collections import defaultdict
from functools import cmp_to_key

ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
ORDER2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def compare(suit1, suit2):
    suit1 = suit1[0]
    suit2 = suit2[0]
    suit1Map = defaultdict(int)
    suit2Map = defaultdict(int)
    for letter in suit1:
        suit1Map[letter] += 1
    for letter in suit2:
        suit2Map[letter] += 1
    suit1Max = 1
    suit2Max = 1
    for key in suit1Map:
        suit1Max = max(suit1Max, suit1Map[key])
    for key in suit2Map:
        suit2Max = max(suit2Max, suit2Map[key])

    if suit1Max != suit2Max:
        return suit1Max - suit2Max
    
    if suit1Max == 3 and suit2Max == 3:
        if 2 in suit1Map.values() and 2 not in suit2Map.values():
            return 1
        if 2 in suit2Map.values() and 2 not in suit1Map.values():
            return -1
        
    if suit1Max == 2 and suit2Max == 2:
        if len(suit1Map) == 3 and len(suit2Map) == 4:
            return 1
        if len(suit2Map) == 3 and len(suit1Map) == 4:
            return -1

    for i in range(len(suit1)):
        char1Rank, char2Rank = ORDER.index(suit1[i]), ORDER.index(suit2[i])
        if char1Rank != char2Rank:
            return -1 * (char1Rank - char2Rank)
    return 0

def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        suitAndBet = []
        lines = f.read().strip().split("\n")
        for line in lines:
            suit, bet = line.split(" ")
            suitAndBet.append((suit, int(bet)))
        
        sortedList = sorted(suitAndBet, key=cmp_to_key(compare))
        total = 0

        for i in range(len(sortedList)):
            total += sortedList[i][1] * (i + 1)

        return total

def compare2(suit1, suit2):
    suit1 = suit1[0]
    suit2 = suit2[0]
    suit1Map = defaultdict(int)
    suit2Map = defaultdict(int)
    for letter in suit1:
        suit1Map[letter] += 1
    for letter in suit2:
        suit2Map[letter] += 1


    suit1JackCount = suit1Map['J']
    suit2JackCount = suit2Map['J']

    del suit1Map['J']
    del suit2Map['J']
    
    suit1Max = 1
    suit2Max = 1
    for key in suit1Map:
        suit1Max = max(suit1Max, suit1Map[key])
    for key in suit2Map:
        suit2Max = max(suit2Max, suit2Map[key])

    suit1Max += suit1JackCount
    suit2Max += suit2JackCount

    if suit1Max != suit2Max:
        return suit1Max - suit2Max
    
    if suit1Max == 3 and suit2Max == 3:
        if len(suit1Map) == 2 and len(suit2Map) == 3:
            return 1
        if len(suit2Map) == 2 and len(suit1Map) == 3:
            return -1
        
    if suit1Max == 2 and suit2Max == 2:
        if len(suit1Map) == 3 and len(suit2Map) == 4:
            return 1
        if len(suit2Map) == 3 and len(suit1Map) == 4:
            return -1

    for i in range(len(suit1)):
        char1Rank, char2Rank = ORDER2.index(suit1[i]), ORDER2.index(suit2[i])
        if char1Rank != char2Rank:
            return -1 * (char1Rank - char2Rank)
    return 0

def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        suitAndBet = []
        lines = f.read().strip().split("\n")
        for line in lines:
            suit, bet = line.split(" ")
            suitAndBet.append((suit, int(bet)))
        
        sortedList = sorted(suitAndBet, key=cmp_to_key(compare2))
        total = 0

        for i in range(len(sortedList)):
            total += sortedList[i][1] * (i + 1)

        return total


if __name__ == "__main__":
    input_path = "./day07/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))