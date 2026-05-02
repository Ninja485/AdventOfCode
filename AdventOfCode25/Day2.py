def day2Part1():
    lista = []
    invalidIds = 0
    with open("inputDay2.txt") as file:
        for line in file:
            lista += line.split(",")

    for elem in lista:
        firstId = int(elem.split("-")[0])
        secondId = int(elem.split("-")[1])
        while(firstId<=secondId):
            if invalidId(firstId):
                invalidIds +=1
            firstId +=1

    return invalidIds

def invalidId(number):
    cadena = str(number)

    return True

print(day2Part1())