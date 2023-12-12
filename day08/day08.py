def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        moves = lines[0]

        print(moves)

        map = {}

        for line in lines[2:]:
            source, left, right = line[0:3], line[7:10], line[12:15]
            map[source] = (left, right)

        count = 0
        curr = 'AAA'

        while True:
            if curr == 'ZZZ':
                break
            
            currMove = moves[count % len(moves)]
            count += 1

            if currMove == 'L':
                curr = map[curr][0]
            else:
                curr = map[curr][1]

        return count

            

def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")


if __name__ == "__main__":
    input_path = "./day08/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))