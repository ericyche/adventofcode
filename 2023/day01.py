def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    sum = 0
    for line in lines: 
        left, right = 0, len(line) - 1
        while not line[left].isdigit():
            left += 1
        while not line[right].isdigit():
            right -= 1
        sum += int(line[left] + line[right])
    return sum

def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    sum = 0

    for line in lines:
        left, right = 0, len(line)
        leftDigit, rightDigit = "", ""
        while True:
            if line[left].isdigit():
                leftDigit = int(line[left])
                break
            elif line[left:left + 3] in nums:
                leftDigit = nums[line[left:left + 3]]
                break
            elif line[left:left + 4] in nums:
                leftDigit = nums[line[left:left + 4]]
                break
            elif line[left:left + 5] in nums:
                leftDigit = nums[line[left:left + 5]]
                break
            else:
                left += 1

        while True:
            if line[right-1].isdigit():
                rightDigit = int(line[right-1])
                break
            if line[right - 3: right] in nums:
                rightDigit = nums[line[right - 3: right]]
                break
            elif line[right - 4: right] in nums:
                rightDigit = nums[line[right - 4: right]]
                break
            elif line[right - 5: right] in nums:
                rightDigit = nums[line[right - 5: right]]
                break
            else:
                right -= 1
        sum += leftDigit * 10 + rightDigit
    return sum



if __name__ == "__main__":
    input_path = "./day01/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))