def partOne():
    nice = 0
    naughtyCombos = ['ab', 'cd', 'pq', 'xy']
    with open('input.txt') as file:
        for line in file:
            if not any(map(line.__contains__, naughtyCombos)):
                if line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u') >= 3:
                    prev = ''
                    for char in line:
                        if char == prev:
                            nice += 1
                            break
                        prev = char
    print(nice)


def partTwo():
    nice = 0
    with open('input.txt') as file:
        for line in file:
            pairs = []
            ok = False
            for i in range(len(line)):
                if i != len(line):
                    pairs.append(line[i:i+2])
            for pair in pairs:
                if len(pair) == 2 and line.count(pair) > 1:
                    index = line.find(pair)
                    if line.count(pair) == 2 and line[index+1:index+2] == pair and line[index+2:index+3] != pair:
                        ok = False
                    else:
                        ok = True
            if ok:
                prev = ''
                prevprev = ''
                for char in line:
                    if char == prevprev:
                        nice += 1
                        break
                    prevprev = prev
                    prev = char
    print(nice)


partOne()
partTwo()
