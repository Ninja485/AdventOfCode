import re


def read_input(filename):
    with open(filename) as f:
        return f.read().strip().splitlines()
    return result


def part1(data):
    count = 0
    for string in data:
        duplicates = re.search(r'([a-z])\1', string)
        vowels = re.findall(r'[aeiouAEIOU]', string)
        followingChar = re.search(r'ab|cd|pq|xy', string)
        if duplicates and len(vowels) >= 3 and not followingChar:
            count += 1
    return count


def part2(data):
    count = 0
    for string in data:
        containsPair = re.search(r'([a-z]{2}).*\1',string)
        containsBetween = re.search(r'([a-z]).\1',string)
        if(containsPair and containsBetween):
            count += 1
    return count


def main():
    data = read_input("inputDay4.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
