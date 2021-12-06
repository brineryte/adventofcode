import math

from numpy.ma import absolute


def printGrid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()


def countOverlaps(grid):
    count = 0
    for row in grid:
        for item in row:
            if item != '.' and item > 1:
                count += 1
    return count


with open('../inputs/input5.txt') as f:
    lines = f.read().splitlines()

    segments = []
    for line in lines:
        coords = line.replace(' ', '').split('->')
        segments.append([int(x) for x in coords[0].split(',')] + [int(x) for x in coords[1].split(',')])
        # # only consider horizontal/vertical
        # if start[0] == end[0] or start[1] == end[1]:
        #     print(start, end)

    gridSize = max([max(x) for x in segments]) + 1

    grid = []
    for i in range(gridSize):
        grid.append([])
        for j in range(gridSize):
            grid[i].append('.')

    # horizontal/vertical only
    #for segment in filter(lambda val: val[0] == val[2] or val[1] == val[3], segments):
    for segment in segments:
        x1, y1, x2, y2 = segment

        if x1 > x2:
            xDist = range(x1, x2 - 1, -1)
        else:
            xDist = range(x1, x2 + 1)
        if y1 > y2:
            yDist = range(y1, y2 - 1, -1)
        else:
            yDist = range(y1, y2 + 1)

        xCoords = []
        for x in xDist:
            xCoords.append(x)

        yCoords = []
        for y in yDist:
            yCoords.append(y)

        print(xCoords, yCoords)

        if len(xCoords) > 1 and len(yCoords) > 1:
            for i, x in enumerate(xCoords):
                if grid[x][yCoords[i]] == '.':
                    grid[x][yCoords[i]] = 0
                grid[x][yCoords[i]] += 1
        elif len(xCoords) > 1:
            for x in xCoords:
                if grid[x][yCoords[0]] == '.':
                    grid[x][yCoords[0]] = 0
                grid[x][yCoords[0]] += 1
        else:
            for y in yCoords:
                if grid[xCoords[0]][y] == '.':
                    grid[xCoords[0]][y] = 0
                grid[xCoords[0]][y] += 1

    printGrid(grid)
    print('part one:', countOverlaps(grid))
