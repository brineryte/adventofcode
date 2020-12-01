import math

def partOne():
    pos = [0, 0]
    facing = 0
    with open('input.txt') as file:
        instructions = file.read().replace(" ", "").split(",")

        for instruction in instructions:
            direction = instruction[0]
            distance = instruction[1:]

            if direction == "L":
                facing -= 1
            elif direction == "R":
                facing += 1

            if facing == -1 or facing == 3:
                facing = 3
                pos[0] -= int(distance)
            elif facing == 4 or facing == 0:
                facing = 0
                pos[1] += int(distance)
            elif facing == 1:
                pos[0] += int(distance)
            elif facing == 2:
                pos[1] -= int(distance)

        print(pos)
        print(math.fabs(pos[0]) + math.fabs(pos[1]))

    print()


def partTwo():
    pos = [0, 0]
    facing = 0
    history = ['0,0']
    with open('input.txt') as file:
        instructions = file.read().replace(" ", "").split(",")

        for instruction in instructions:
            direction = instruction[0]
            distance = instruction[1:]

            if direction == "L":
                facing -= 1
            elif direction == "R":
                facing += 1

            if facing == -1 or facing == 3:
                facing = 3
                for point in range(int(distance)):
                    pos[0] -= 1
                    posKey = f'{pos[0]},{pos[1]}'
                    if history.count(posKey) > 0:
                        break
                    history.append(posKey)
            elif facing == 4 or facing == 0:
                facing = 0
                for point in range(int(distance)):
                    pos[1] += 1
                    posKey = f'{pos[0]},{pos[1]}'
                    if history.count(posKey) > 0:
                        break
                    history.append(posKey)
            elif facing == 1:
                for point in range(int(distance)):
                    pos[0] += 1
                    posKey = f'{pos[0]},{pos[1]}'
                    if history.count(posKey) > 0:
                        break
                    history.append(posKey)
            elif facing == 2:
                for point in range(int(distance)):
                    pos[1] -= 1
                    posKey = f'{pos[0]},{pos[1]}'
                    if history.count(posKey) > 0:
                        break
                    history.append(posKey)

        print(history)
        print(pos)
        print(math.fabs(pos[0]) + math.fabs(pos[1]))



partOne()
partTwo()

def test():
    history = ['0,1', '0,1', '0,1']
    print(history.count('0,1'))

test()