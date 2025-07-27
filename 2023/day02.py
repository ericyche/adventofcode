def part_one(filename):
    RED = 12
    GREEN = 13
    BLUE = 14
    total = 0
    with open(filename, encoding="utf-8") as f:
        fileList = f.read().splitlines()
        for line in fileList:
            game, cubes = line.split(":")
            gameNum, cubeGameList = int(game[5:]), cubes.split(";")
            validGame = True

            for cubeGame in cubeGameList:
                cubes = cubeGame.split(",")
                for i in range(len(cubes)):
                    cubes[i] = cubes[i].strip(" ").split(" ")
                    cubes[i][0] = int(cubes[i][0])

                for cube in cubes:
                    if cube[1] == 'red' and cube[0] > RED:
                        validGame = False
                    if cube[1] == 'green' and cube[0] > GREEN:
                        validGame = False
                    if cube[1] == 'blue' and cube[0] > BLUE:
                        validGame = False

            if validGame:
                total += gameNum
    return total


def part_two(filename: str) -> int:
    total = 0
    with open(filename, encoding="utf-8") as f:
        fileList = f.read().splitlines()
        for line in fileList:
            game, cubes = line.split(":")
            gameNum, cubeGameList = int(game[5:]), cubes.split(";")
            redMin, blueMin, greenMin = 1, 1, 1

            for cubeGame in cubeGameList:
                cubes = cubeGame.split(",")
                for i in range(len(cubes)):
                    cubes[i] = cubes[i].strip(" ").split(" ")
                    cubes[i][0] = int(cubes[i][0])

                for cube in cubes:
                    if cube[1] == 'red':
                        redMin = max(redMin, cube[0])
                    if cube[1] == 'green':
                        greenMin = max(greenMin, cube[0])
                    if cube[1] == 'blue':
                        blueMin = max(blueMin, cube[0])

            # print("Red: " + str(redMin) + "Blue: " + str(blueMin) + "Green: " + str(greenMin))
            total += redMin * blueMin * greenMin
    return total


if __name__ == "__main__":
    input_path = "./day02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))