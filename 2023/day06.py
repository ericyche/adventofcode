def part_one(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        times, dist = [int(time) for time in lines[0].split()[1:]], [int(dist) for dist in lines[1].split()[1:]]
        timeDistPairs = tuple(zip(times, dist))
        product = 1
        for time, dist in timeDistPairs:
            numValid = 0
            for timeHeld in range(0, time+1):
                travelDist = timeHeld * (time - timeHeld)
                if travelDist > dist:
                    numValid += 1
            if numValid > 0:
                product *= numValid
        return product
        
def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        time = int(lines[0].replace(" ", "").split(":")[1])
        dist = int(lines[1].replace(" ", "").split(":")[1]) 
        numValid = 0
        for timeHeld in range(0, time+1):
            travelDist = timeHeld * (time - timeHeld)
            if travelDist > dist:
                numValid += 1
        return numValid

if __name__ == "__main__":
    input_path = "./day06/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))