import hashlib


def read_input(filename):
    with open(filename) as f:
        return f.read().strip()
    return result

def generalFunction(key,lenDemanded):
    number = 0
    while hashlib.md5((key + str(number)).encode()).hexdigest()[:lenDemanded] != "0"*lenDemanded:
        number += 1
    return number

def part1(key):
    number = 0
    while hashlib.md5((key + str(number)).encode()).hexdigest()[:5] != "00000":
        number += 1
    return number

def part2(key):
    number = 0
    while hashlib.md5((key + str(number)).encode()).hexdigest()[:6] != "000000":
        number += 1
    return number


def main():
    data = "bgvyzdsv"
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
