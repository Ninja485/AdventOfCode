from re import match


def read_input(filename):
    with open(filename) as f:
        return f.read().strip()
    return result


def part1(data):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))

    for c in data:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1

        visited.add((x, y))

    return len(visited)


def part2(data):
    santaX,santaY = 0,0
    roboSantaX,roboSantaY = 0,0
    visited = set()
    visited.add((0,0))
    santaTurn = True
    for c in data:
        if c == '^':
            if(santaTurn):
                santaTurn = False
                santaY +=1
            else:
                santaTurn = True
                roboSantaY +=1

        elif c == 'v':
            if (santaTurn):
                santaTurn = False
                santaY -= 1
            else:
                santaTurn = True
                roboSantaY -= 1
        elif c == '>':
            if (santaTurn):
                santaTurn = False
                santaX += 1
            else:
                santaTurn = True
                roboSantaX += 1
        elif c == '<':
            if (santaTurn):
                santaTurn = False
                santaX -= 1
            else:
                santaTurn = True
                roboSantaX -= 1

        visited.add((santaX, santaY))
        visited.add((roboSantaX,roboSantaY))
    return len(visited)


def main():
    data = read_input("inputDay3.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
