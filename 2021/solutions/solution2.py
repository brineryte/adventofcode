with open("../inputs/input2.txt") as f:
    lines = f.read().splitlines()
    pos = [0, 0]
    for line in lines:
        direction, dist = line.split(' ')
        if direction == 'down':
            pos[0] += int(dist)
        elif direction == 'up':
            pos[0] -= int(dist)
        else:
            pos[1] += int(dist)

    print(pos[0] * pos[1])

with open("../inputs/input2.txt") as f:
    lines = f.read().splitlines()
    pos = [0, 0]
    aim = 0
    for line in lines:
        direction, dist = line.split(' ')
        if direction == 'down':
            aim += int(dist)
        elif direction == 'up':
            aim -= int(dist)
        else:
            pos[1] += int(dist)
            pos[0] += aim*int(dist)

    print(pos[0] * pos[1])
