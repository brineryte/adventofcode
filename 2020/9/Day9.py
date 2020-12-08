def partOne():
    data = getParsedInputData()


def partTwo():
    data = getParsedInputData()


def getParsedInputData(inputData="input.txt"):
    with open(inputData) as file:
        data = file.read()
    file.close()

    # Do some logic

    return data


partOne()
partTwo()

