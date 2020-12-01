from colorama import Fore, Back, Style


def partOne(lights, instructions, printOut=False):

    with open(instructions) as file:
        for line in file:
            command = getCommandFromInput(line)
            updateLights(command["action"], lights, command["x1"], command["y1"], command["x2"], command["y2"])

    if printOut:
        for x in lights:
            for y in x:
                if y == "x":
                    print(Fore.LIGHTGREEN_EX + y, end="")
                else:
                    print(Fore.RED + y, end="")
            print()

    print(countLights(lights))


def partTwo(lights, instructions):
    with open(instructions) as file:
        for line in file:
            command = getCommandFromInput(line)
            updateLights2(command["action"], lights, command["x1"], command["y1"], command["x2"], command["y2"])

    total = 0
    for x in lights:
        for y in x:
            total += int(y)

    print(total)


def countLights(lights):
    count = 0
    for x in lights:
        for y in x:
            if y == "x":
                count += 1
    return count


def updateLights(command, lights, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if command == "toggle":
                if lights[x][y] == "x":
                    lights[x][y] = "."
                else:
                    lights[x][y] = "x"
            elif command == "on":
                lights[x][y] = "x"
            else:
                lights[x][y] = "."


def updateLights2(command, lights, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if command == "toggle":
                lights[x][y] += 2
            elif command == "on":
                lights[x][y] += 1
            else:
                if lights[x][y] > 0:
                    lights[x][y] -= 1


def getCommandFromInput(line):
    line = line.rstrip("\n").rstrip(" ")

    commandParts = line.split(" ")

    if commandParts[0] == "turn":
        commandParts.remove("turn")

    action = commandParts[0]
    x1 = int(commandParts[1].split(",")[0])
    x2 = int(commandParts[3].split(",")[0])

    y1 = int(commandParts[1].split(",")[1])
    y2 = int(commandParts[3].split(",")[1])

    return {"action": action, "x1": x1, "x2": x2, "y1": y1, "y2": y2}


partOne([['.']*1000 for _ in range(1000)], 'input.txt')
partTwo([[0]*1000 for _ in range(1000)], 'input.txt')