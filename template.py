def part_1(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            print(line)

def part_2(filename):
     with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            print(line)

if __name__ == "__main__":
    input_path_1 = "input1.txt"
    input_path_2 = "input1.txt"
    print("---Part One---")
    print(part_1(input_path_1))

    print("---Part Two---")
    print(part_2(input_path_2))
