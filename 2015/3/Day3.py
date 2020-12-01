
def partOne():
    with open('input.txt') as file:
        instructions = file.read()
        houses = executeInstructions(instructions)

    print(len(houses))


def partTwo():
    with open('input.txt') as file:
        instructions = file.read()

        santaPath = instructions[::2]
        roboPath: str = instructions[1::2]

        santaHouses = executeInstructions(santaPath)
        roboHouses = executeInstructions(roboPath)

        print(len(santaHouses.union(roboHouses)))


def executeInstructions(instructions):
    houses = [(0, 0)]
    for step in instructions:
        x = houses[-1][0]
        y = houses[-1][1]
        if step == ">":
            y += 1
        elif step == "^":
            x += 1
        elif step == "v":
            x -= 1
        elif step == "<":
            y -= 1
        houses.append((x, y))
    return set(houses)


partOne()
partTwo()
