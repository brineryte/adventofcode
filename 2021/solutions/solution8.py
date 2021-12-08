_ = ''
a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'

alphabet = [a, b, c, d, e, f, g]
cipherAlphabet = [_, _, _, _, _, _, _]

numbers = [{a, b, c, e, f, g},
           {c, f},
           {a, c, d, e, g},
           {a, c, d, f, g},
           {b, c, d, f},
           {a, b, d, f, g},
           {a, b, d, e, f, g},
           {a, c, f},
           {a, b, c, d, e, f, g},
           {a, b, c, d, f, g}]


def getNumber(num):
    return numbers[num]


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

        cipherNumbers = [set() for x in range(10)]
        results = []
        for line in data:
            parts = line.split('|')
            digits = parts[0].strip().split(' ')

            # determine 1, 4, 7, 8 by length
            for digit in digits:
                if len(digit) == 2:
                    cipherNumbers[1] = set(digit)
                elif len(digit) == 3:
                    cipherNumbers[7] = set(digit)
                elif len(digit) == 4:
                    cipherNumbers[4] = set(digit)
                elif len(digit) == 7:
                    cipherNumbers[8] = set(digit)

            # get the rest
            for digit in digits:
                if cipherNumbers[4].issubset(set(digit)) and len(digit) == 6:
                    cipherNumbers[9] = set(digit)
                elif cipherNumbers[7].issubset(set(digit)) and len(digit) == 6:
                    cipherNumbers[0] = set(digit)
                elif len(digit) == 6:
                    cipherNumbers[6] = set(digit)
                elif cipherNumbers[7].issubset(set(digit)) and len(digit) == 5:
                    cipherNumbers[3] = set(digit)

            # get 5 and 2
            for digit in digits:
                if set(digit).issubset(cipherNumbers[9]) and not cipherNumbers[7].issubset(set(digit)) and len(digit) == 5:
                    cipherNumbers[5] = set(digit)
                elif not cipherNumbers[7].issubset(set(digit)) and len(digit) == 5:
                    cipherNumbers[2] = set(digit)

            output = parts[1].strip().split(' ')
            result = ''
            for digit in output:
                if set(digit) in cipherNumbers:
                    result = result + str(cipherNumbers.index(set(digit)))

            results.append(int(result))
        print(sum([x for x in results]))


partOne()
partTwo()
