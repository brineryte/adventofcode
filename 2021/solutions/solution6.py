def partOne():
    with open('../inputs/input6.txt') as f:
        data = f.read().split(',')
        initial = [int(x) for x in data]

        for day in range(80):
            current = initial.copy()
            for i, fish in enumerate(current):
                if fish == 0:
                    initial.append(8)
                    initial[i] = 6
                else:
                    initial[i] -= 1

        print(len(initial))


def partTwo():
    with open('../inputs/input6.txt') as f:
        data = f.read().split(',')
        initial = [int(x) for x in data]

        counts = dict()
        for i in range(9):
            counts[i] = 0

        for i in initial:
            counts[i] += 1

        for day in range(256):
            currentCounts = counts.copy()
            for i in range(9):
                counts[i] = currentCounts[i + 1 if i < 8 else 0]
                if i == 8:
                    counts[6] += counts[i]

        print(sum(counts.values()))


print('Part one:', end='\n')
partOne()
print()
print('Part two:', end='\n')
partTwo()
