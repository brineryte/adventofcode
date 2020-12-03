import math


def partOne():
    with open("input.txt") as baseMap:
        baseMap = list(baseMap)
        treeCount = countTreesOnSlope(baseMap, 3)
        print(treeCount)


def partTwo():
    with open("input.txt") as baseMap:
        baseMap = list(baseMap)
        count1 = countTreesOnSlope(baseMap, 1)
        count2 = countTreesOnSlope(baseMap, 3)
        count3 = countTreesOnSlope(baseMap, 5)
        count4 = countTreesOnSlope(baseMap, 7)
        count5 = countTreesOnSlope(baseMap, 1, 2)

    print(math.prod([count1,count2,count3,count4,count5]))


def countTreesOnSlope(baseMap, increment, verticalIncrement=1):

    start = 0 - increment
    treeCount = 0

    for row in baseMap[::verticalIncrement]:
        mapRow = row.rstrip("\n")

        start += increment

        if start >= len(mapRow):
            start -= len(mapRow)

        if mapRow[start] == "#":
            treeCount += 1

    return treeCount


partOne()
partTwo()
