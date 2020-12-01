def partOne():
    with open('input2015.txt') as file:
        puzzleInput = file.read()

    floor = 0
    for element in puzzleInput:
        if element == "(":
            floor += 1
        elif element == ")":
            floor -=1

    print(str(floor))


def partTwo():
    with open('input2015.txt') as file:
        puzzleInput = file.read()

    floor = 0
    position = 1
    for element in puzzleInput:
        if element == "(":
            floor += 1
        elif element == ")":
            floor -=1

        if floor == -1:
            print(position)
            return 0

        position += 1

partOne()
partTwo()
