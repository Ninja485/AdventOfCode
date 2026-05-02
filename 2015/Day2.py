import heapq
def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            a, b, c = map(int, line.strip().split('x'))
            result.append((a, b, c))
    return result

def part1(data):
    requiredPaper = 0
    for l,w,h in data:
        two_smallest = heapq.nsmallest(2, [l,w,h])
        requiredPaper += 2*l*w + 2*w*h + 2*h*l + two_smallest[0]*two_smallest[1]
    return  requiredPaper




def part2(data):
    feetRibbon = 0
    for l, w, h in data:
        two_smallest = heapq.nsmallest(2, [l, w, h])
        feetRibbon += two_smallest[0]*2 + two_smallest[1] *2 + l*w*h
    return feetRibbon


def main():
    data = read_input("inputDay2.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()