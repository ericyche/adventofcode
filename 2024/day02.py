def is_safe(num_list):
    for i in range(1, len(num_list)):
        diff = num_list[i] - num_list[i - 1]
        if diff <= 0 or diff > 3:
            return False
    return True

def part_1(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        total = 0
        for line in lines:
            num_list = [int(num) for num in line.split()]
            is_safe_result = is_safe(num_list) or is_safe(num_list[::-1])
            total += 1 if is_safe_result else 0
        return total

def part_2(filename):
     def is_safe_with_damp(num_list):
        if is_safe(num_list):
            return True
        for i in range(0, len(num_list)):
            list_without_num = num_list[:i] + num_list[i+1:]
            if is_safe(list_without_num):
                return True
        return False 
                
     with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        total = 0
        for line in lines:
            num_list = [int(num) for num in line.split()]
            is_safe_result = is_safe_with_damp(num_list) or is_safe_with_damp(num_list[::-1])
            total += 1 if is_safe_result else 0
        return total

if __name__ == "__main__":
    input_path_1 = "2024/input02.txt"
    input_path_2 = "2024/input02.txt"
    print("---Part One---")
    print(part_1(input_path_1))

    print("---Part Two---")
    print(part_2(input_path_2))