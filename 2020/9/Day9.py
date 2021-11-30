def partOne():
    data = getParsedInputData().split("\n")
    the_number = 0
    for index, number in enumerate(data):
        if index >= 25:
            ok = False
            for i in data[index-25:index]:
                if str(int(number) - int(i)) in data[index-25:index]:
                    ok = True
            if not ok:
                the_number = number
    print(the_number)
    return the_number


def partTwo():
    the_number = int(partOne())

    data = getParsedInputData().split("\n")
    number_list = [int(i) for i in data]

    the_index = number_list.index(the_number)

    contiguous = []
    for index, number in enumerate(number_list[:the_index]):
        for n in number_list[index:the_index]:
            contiguous.append(n)
            if sum(contiguous) == the_number:
                print(min(contiguous) + max(contiguous))
            if sum(contiguous) > the_number:
                contiguous.clear()
                break



def getParsedInputData(inputData="input.txt"):
    with open(inputData) as file:
        data = file.read()
    file.close()

    # Do some logic

    return data


first_number = partOne()
partTwo()

