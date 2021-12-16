import itertools

from colorama import Fore
from colorama import Style


def printOctopi(data):
    for i in data:
        for j in i:
            if 0 < j < 10:
                print(j, end=' ')
            else:
                print(f'{Fore.RED}{j}{Style.RESET_ALL}', end=' ')
        print()


def runFlashes(data, step):
    # print()
    flashCount = 0
    for i, line in enumerate(data):
        for j, octopus in enumerate(line):
            data[i][j] += 1

    while 10 in list(itertools.chain.from_iterable(data)):
        for i, line in enumerate(data):
            for j, octopus in enumerate(line):
                if data[i][j] == 10:
                    data[i][j] = 0

                    if i > 0 and j > 0 and 0 < data[i - 1][j - 1] < 10:
                        data[i - 1][j - 1] += 1
                    if i > 0 and 0 < data[i - 1][j] < 10:
                        data[i - 1][j] += 1
                    if i > 0 and j < len(line) - 1 and 0 < data[i - 1][j + 1] < 10:
                        data[i - 1][j + 1] += 1
                    if j > 0 and 0 < data[i][j - 1] < 10:
                        data[i][j - 1] += 1
                    if j < len(line) - 1 and 0 < data[i][j + 1] < 10:
                        data[i][j + 1] += 1
                    if i < len(data) - 1 and j > 0 and 0 < data[i + 1][j - 1] < 10:
                        data[i + 1][j - 1] += 1
                    if i < len(data) - 1 and 0 < data[i + 1][j] < 10:
                        data[i + 1][j] += 1
                    if i < len(data) - 1 and j < len(line) - 1 and 0 < data[i + 1][j + 1] < 10:
                        data[i + 1][j + 1] += 1

    # printOctopi(data)
    if list(itertools.chain.from_iterable(data)).count(0) == len(list(itertools.chain.from_iterable(data))):
        print(step)
    return list(itertools.chain.from_iterable(data)).count(0)


with open('../inputs/input11.txt') as f:
    data = f.read().splitlines()

    formattedData = []
    for line in data:
        formatted = [int(x) for x in line]
        formattedData.append(formatted)

    flashes = 0
    for i in range(300):
        flashes += runFlashes(formattedData, i)

    print(flashes)
