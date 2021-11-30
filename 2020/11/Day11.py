def partOne():
    data = getParsedInputData()
    rows = data.split("\n")

    for i, row in enumerate(rows):
        rows[i] = list(rows[i])

    fillSeats(rows)


def fillSeats(rows):
    count = 0
    newRows = rows.copy()
    while True:
        for i, row in enumerate(rows):
            for j, seat in enumerate(row):
                nearBySeats = getNearbySeats(i, j, rows)
                if seat == "L" and nearBySeats.count("#") == 0:
                    newRows[i][j] = "#"
                elif seat == "#" and nearBySeats.count("#") > 3:
                    newRows[i][j] = "L"

        newCount = countOccupiedSeats(newRows)
        if count == newCount:
            print(count)
            break
        rows.clear()
        rows = newRows.copy()
        count = newCount


def countOccupiedSeats(rows):
    count = 0
    for seats in rows:
        count += seats.count("#")
    return count


def getNearbySeats(i, j, rows):
    try:
        uL = rows[i - 1][j - 1]
    except IndexError:
        uL = ""
    try:
        u = rows[i - 1][j]
    except IndexError:
        u = ""
    try:
        uR = rows[i - 1][j + 1]
    except IndexError:
        uR = ""
    try:
        b = rows[i][j - 1]
    except IndexError:
        b = ""
    try:
        a = rows[i][j + 1]
    except IndexError:
        a = ""
    try:
        dL = rows[i + 1][j - 1]
    except IndexError:
        dL = ""
    try:
        d = rows[i + 1][j]
    except IndexError:
        d = ""
    try:
        dR = rows[i + 1][j + 1]
    except IndexError:
        dR = ""

    return [uL, u, uR, b, a, dL, d, dR]


def isOccupied(seat):
    return seat == "#"


def partTwo():
    data = getParsedInputData()


def getParsedInputData(inputData="input2.txt"):
    with open(inputData) as file:
        data = file.read()
    file.close()

    # Do some logic

    return data


partOne()
partTwo()

