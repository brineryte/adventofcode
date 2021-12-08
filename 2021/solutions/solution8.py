cNums = [set() for x in range(10)]


def isSubset(n, m):
    return cNums[n].issubset(set(m))


def partOne():
    print("Part one: ")
    with open('../inputs/input8.txt') as f:
        data = f.read().splitlines()

        count = 0
        for line in data:
            parts = line.split('|')
            output = parts[1].strip().split(' ')
            for digit in output:
                if len(digit) in [2, 3, 4, 7]:
                    count += 1
        print(count)
    print()


def partTwo():
    print("Part two: ")
    with open('../inputs/input8.txt') as f:
        data = f.read().splitlines()

        results = []
        for line in data:
            parts = line.split('|')
            digits = parts[0].strip().split(' ')

            # determine 1, 4, 7, 8 by length
            for digit in digits:
                if len(digit) == 2:
                    cNums[1] = set(digit)
                elif len(digit) == 3:
                    cNums[7] = set(digit)
                elif len(digit) == 4:
                    cNums[4] = set(digit)
                elif len(digit) == 7:
                    cNums[8] = set(digit)
            # get the rest
            for digit in digits:
                if isSubset(4, digit) and len(digit) == 6:
                    cNums[9] = set(digit)
                elif isSubset(7, digit) and len(digit) == 6:
                    cNums[0] = set(digit)
                elif len(digit) == 6:
                    cNums[6] = set(digit)
                elif isSubset(7, digit) and len(digit) == 5:
                    cNums[3] = set(digit)
            # get 5 and 2
            for digit in digits:
                if set(digit).issubset(cNums[9]) and not isSubset(7, digit) and len(digit) == 5:
                    cNums[5] = set(digit)
                elif not isSubset(7, digit) and len(digit) == 5:
                    cNums[2] = set(digit)

            output = parts[1].strip().split(' ')
            result = ''
            for digit in output:
                if set(digit) in cNums:
                    result = result + str(cNums.index(set(digit)))

            results.append(int(result))
        print(sum(results))
    print()


partOne()
partTwo()
