# * Part One
with open('../inputs/input7.txt') as f:
    data = [int(x) for x in f.read().split(',')]

    cheapestPos = 0
    cheapestCost = 0
    pos = 0
    while True:
        cost = 0
        for crab in data:
            cost += abs(pos - crab)

        if cheapestCost == 0 or cheapestCost > cost:
            cheapestPos = pos
            cheapestCost = cost
        elif cheapestCost < cost:
            break

        pos += 1

    print("Part ONE: ", end='\n')
    print(cheapestPos)
    print(cheapestCost, end='\n\n')


# * Not Elegant at all Part Two
    cheapestPos = 0
    cheapestCost = 0
    pos = 0
    while True:
        cost = 0
        for crab in data:
            dist = abs(pos - crab)
            for d in range(dist):
                cost += d + 1

        if cheapestCost == 0 or cheapestCost > cost:
            cheapestPos = pos
            cheapestCost = cost
        elif cheapestCost < cost:
            break

        pos += 1

    print("Part TWO: ", end='\n')
    print(cheapestPos)
    print(cheapestCost)
