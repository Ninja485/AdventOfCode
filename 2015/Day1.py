from itertools import takewhile
def read_input(filename):
    with open(filename) as f:
        return f.read().strip()

def part1(data):
    return data.count('(') - data.count(')')


def part2(data):
    charPosition = 0
    floor = 0
    iteratorData = iter(range(len(data)))

    for index in takewhile(lambda index: floor != -1,iteratorData):
        if(data[index] == "("):
            floor += 1
        elif(data[index] == ")"):
            floor -= 1
        charPosition += 1
    return charPosition


def main():
    data = read_input("inputDay1Part1.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()