# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def day1Part1():
    contador=0;
    currentPosition = 50
    with open("inputDay1.txt") as file:
        for line in file:
            direction = line[:1]
            movements = int(line[1:]) % 100
            if(direction == 'L'):
                movements = -1*movements
            if(currentPosition+movements < 0):
                currentPosition = 100 + (currentPosition + movements) % 100;
            elif(currentPosition+movements>=100):
                currentPosition = (currentPosition+movements)%100
            else:
                currentPosition += movements
            if(currentPosition == 0):
                contador += 1
    return contador

def day1Part2():
    contador = 0
    currentPosition = 50
    with open("inputDay1.txt") as file:
        for line in file:
            direction = line[:1]
            movements = int(line[1:])
            rounds = movements // 100
            movements %= 100

            if (direction == 'L'):
                movements = -1 * movements
            if (currentPosition + movements < 0):
                if(currentPosition != 0):
                    contador+=1
                currentPosition = 100 + (currentPosition + movements);
            elif (currentPosition + movements >= 100):
                currentPosition = (currentPosition + movements) % 100
                contador +=1
            else:
                currentPosition += movements
                if(currentPosition == 0):
                    contador +=1
            contador += rounds;
    return contador



print(day1Part1())
print(day1Part2())
