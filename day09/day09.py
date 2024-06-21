def not_all_zeros(nums):
    return all(num == 0 for num in nums)

def extrapolate(nums):
    stk = []
    stk.append(nums)

    while not not_all_zeros(stk[-1]):
        diff = [stk[-1][i] - stk[-1][i-1] for i in range(1, len(stk[-1]))]
        stk.append(diff)
    
    curr_num = 0
    for nums in stk[::-1]:
        curr_num += nums[-1]
    return curr_num

def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        sum = 0
        for line in lines:
            nums = [int(x) for x in line.split(" ")]
            sum += extrapolate(nums)
        return sum


def extrapolate_past(nums):
    stk = []
    stk.append(nums)

    while not not_all_zeros(stk[-1]):
        diff = [stk[-1][i] - stk[-1][i-1] for i in range(1, len(stk[-1]))]
        stk.append(diff)
    
    curr_num = 0
    for nums in stk[::-1]:
        curr_num = nums[0] - curr_num
    return curr_num


def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        sum = 0
        for line in lines:
            nums = [int(x) for x in line.split(" ")]
            sum += extrapolate_past(nums)
        return sum    

if __name__ == "__main__":
    input_path = "./day09/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))