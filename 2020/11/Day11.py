import copy


def partOne():
    rows = getParsedInputData()

    formattedRows = []
    for row in rows:
        formattedRows.append(list(row))

    fillSeats(formattedRows)


def fillSeats(rows):
    count = 0
    newRows = copy.deepcopy(rows)
    while True:
        for i, row in enumerate(rows):
            for j, seat in enumerate(row):
                nearBySeats = getNearbySeats(i, j, rows)
                if seat == "L" and nearBySeats.count("#") == 0:
                    newRows[i][j] = "#"
                elif seat == "#" and nearBySeats.count("#") >= 4:
                    newRows[i][j] = "L"

        newCount = countOccupiedSeats(newRows)
        if count == newCount:
            print(count)
            break
        rows.clear()
        rows = copy.deepcopy(newRows)
        count = newCount


def printWaitingArea(rows):
    for row in rows:
        print(''.join(row))
    print()


def countOccupiedSeats(rows):
    count = 0
    for seats in rows:
        count += seats.count("#")
    return count


def getNearbySeats(i, j, rows):
    try:
        uL = rows[i - 1][j - 1] if j > 0 and i > 0 else "x"
    except IndexError:
        print("out of range")
        uL = "x"
    try:
        u = rows[i - 1][j] if i > 0 else "x"
    except IndexError:
        u = "x"
    try:
        uR = rows[i - 1][j + 1] if i > 0 else "x"
    except IndexError:
        uR = "x"
    try:
        b = rows[i][j - 1] if j > 0 else "x"
    except IndexError:
        b = "x"
    try:
        a = rows[i][j + 1]
    except IndexError:
        a = "x"
    try:
        dL = rows[i + 1][j - 1] if j > 0 else "x"
    except IndexError:
        dL = "x"
    try:
        d = rows[i + 1][j]
    except IndexError:
        d = "x"
    try:
        dR = rows[i + 1][j + 1]
    except IndexError:
        dR = "x"

    return [uL, u, uR, b, a, dL, d, dR]


def isOccupied(seat):
    return seat == "#"


def partTwo():
    data = getParsedInputData()


def getParsedInputData(inputData="input.txt"):
    with open(inputData) as file:
        data = file.read().splitlines()
    file.close()
    # Do some logic
    return data


partOne()
partTwo()
