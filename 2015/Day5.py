import re
def read_input(filename):
    with open(filename) as f:
        return f.read().strip().splitlines()
    return result


def part1(data):
    lightsOn = 0
    lights = []
    for i in range(0,1000):
        row = []
        for j in range(0,1000):
            row.append(False)
        lights.append(row)
    for line in data:
        nums = list(map(int, re.findall(r'\d+', line)))
        columnOrigen = 0
        rowOrigen = 0
        columnDestiny = 0
        rowDestiny = 0
        columnOrigen = nums[0]
        rowOrigen = nums[1]
        columnDestiny = nums[2] + 1
        rowDestiny = nums[3] + 1
        for i in range(rowOrigen,rowDestiny):
            for j in range(columnOrigen,columnDestiny):
                if line.startswith("turn off"):
                    lights[i][j] = False
                elif line.startswith("turn on"):
                     lights[i][j] = True
                else:
                    lights[i][j] = not lights[i][j]
    for i in range(0, 1000):
        for j in range(0, 1000):
           if lights[i][j]:
               lightsOn += 1
    return lightsOn


def part2(data):
    lightsOn = 0
    lights = []
    for i in range(0, 1000):
        row = []
        for j in range(0, 1000):
            row.append(0)
        lights.append(row)
    for line in data:
        nums = list(map(int, re.findall(r'\d+', line)))
        columnOrigen = 0
        rowOrigen = 0
        columnDestiny = 0
        rowDestiny = 0
        columnOrigen = nums[0]
        rowOrigen = nums[1]
        columnDestiny = nums[2] + 1
        rowDestiny = nums[3] + 1
        for i in range(rowOrigen, rowDestiny):
            for j in range(columnOrigen, columnDestiny):
                if line.startswith("turn off"):
                    lights[i][j] = max(0,lights[i][j]-1)
                elif line.startswith("turn on"):
                    lights[i][j] += 1
                else:
                    lights[i][j] += 2
    for i in range(0, 1000):
        for j in range(0, 1000):
            if lights[i][j]:
                lightsOn += lights[i][j]
    return lightsOn



def main():
    data = read_input("inputDay5.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
