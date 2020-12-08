def partOne():
    data = getParsedInputData()

    runBootCode(data)


def partTwo():
    data = getParsedInputData()

    for index in range(0, len(data)):
        newData = list(data)
        if "jmp" in newData[index]:
            newData[index] = newData[index].replace("jmp", "nop")
            runBootCode(newData)
        elif "nop" in newData[index]:
            newData[index] = newData[index].replace("nop", "jmp")
            runBootCode(newData)


def runBootCode(bootCode):
    accumulator = 0
    pos = 0
    history = list()
    while True:
        if pos in history or pos >= len(bootCode):
            if pos >= len(bootCode):
                print("Finished!")
            print(accumulator)
            break

        history.append(pos)

        schnarfl = bootCode[pos].split()

        command = schnarfl[0]
        value = schnarfl[1]

        if command == "acc":
            accumulator += int(value)
            pos += 1
        elif command == "jmp":
            pos += int(value)
        elif command == "nop":
            pos += 1
        else:
            pass
    return accumulator


def getParsedInputData(inputData="input.txt"):
    with open(inputData) as file:
        data = file.read().split("\n")
    file.close()

    # Do some logic

    return data


partOne()
partTwo()

