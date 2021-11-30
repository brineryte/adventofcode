def partOne():
    data = getParsedInputData().split("\n")
    adapters = [int(i) for i in data]
    adapters.sort()

    ones = 1
    twos = 0
    threes = 1
    for i, number in enumerate(adapters[:-1]):
        if adapters[i+1] - number == 3:
            threes += 1
        elif adapters[i+1] - number == 1:
            ones += 1
        elif adapters[i+1] - number == 2:
            twos += 1

    print("Ones:" + str(ones))
    print("Threes:" + str(threes))
    print(ones * threes)


def partTwo():
    data = getParsedInputData().split("\n")
    adapters = [int(i) for i in data]
    adapters.sort()

    print(adapters)
    # maybe use sets or tuples
    # I think the algorithm is this:
    # The first permutation is just all of the numbers
    # after that, go through and figure out which numbers can be removed and have it still work, each one is another permutation
    # loop through again and count how many 2-number runs can be removed, each of these is another permutation


def getParsedInputData(inputData="input3.txt"):
    with open(inputData) as file:
        data = file.read()
    file.close()

    # Do some logic

    return data


partOne()
partTwo()

