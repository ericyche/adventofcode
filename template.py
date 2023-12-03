def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")


def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")


if __name__ == "__main__":
    input_path = "./day00/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))