from collections import Counter

def part_1(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        list1, list2 = [], []
        for line in lines:
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))

        list1.sort()
        list2.sort()

        assert len(list1) == len(list2), "Lists must be of equal length"

        total_diff = 0
        for i in range(len(list1)):
            total_diff += abs(list1[i] - list2[i])
            
        return total_diff

def part_2(filename):
     with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        list1, list2 = [], []
        for line in lines:
            num1, num2 = line.split()
            list1.append(int(num1))  
            list2.append(int(num2))

        list2_counter = Counter(list2)
        similarity_score = 0

        for num in list1:
            if num in list2_counter:
                similarity_score += num * list2_counter[num]

        return similarity_score


if __name__ == "__main__":
    input_path_1 = "input1.txt"
    input_path_2 = "input1.txt"
    print("---Part One---")
    print(part_1(input_path_1))

    print("---Part Two---")
    print(part_2(input_path_2))