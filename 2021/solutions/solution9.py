with open('../inputs/input9.txt') as f:
    data = f.read().splitlines()
    riskLevels = []
    lowPoints = []
    for i, line in enumerate(data):
        for j, point in enumerate(line):
            north, south, east, west = 10, 10, 10, 10
            if i > 0:
                north = int(data[i - 1][j])
            if i < len(data) - 1:
                south = int(data[i + 1][j])
            if j > 0:
                west = int(data[i][j - 1])
            if j < len(line) - 1:
                east = int(data[i][j + 1])

            intPoint = int(point)
            if intPoint < north and intPoint < south and intPoint < west and intPoint < east:
                riskLevels.append(1 + intPoint)
                lowPoints.append([i, j])

    print(sum(riskLevels))
    basinSizes = []
    for start in lowPoints:
        i, j = start[0], start[1]
        unverified = [[i, j]]
        verified = []
        size = 0
        while len(unverified) > 0:
            x, y = unverified[0][0], unverified[0][1]
            if (unverified[0] not in verified) and x > -1 and y > -1 and x < len(data) \
                    and y < len(data[0]) and int(data[x][y]) != 9:
                size += 1
                del(unverified[0])
                verified.append([x, y])
                for point in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    unverified.append(point)
            else:
                del(unverified[0])
                verified.append([x, y])

        basinSizes.append(size)

    basinSizes.sort(reverse=True)
    print(basinSizes[0] * basinSizes[1] * basinSizes[2])
