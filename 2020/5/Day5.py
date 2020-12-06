

def partOne():
    seatIds = getSeats()
    print(max(seatIds))


def partTwo():
    seatIds = getSeats()
    seatIds.sort()
    potential = []
    for i in range(0, len(seatIds)-1):
        if seatIds[i] + 1 != seatIds[i+1]:
            potential.append(seatIds[i]+1)

    print(potential)


def getSeats():
    seatIds = []
    with open("input.txt") as file:
        for line in file:
            rowCeil = 128
            rowFloor = 0
            seatCeil = 8
            seatFloor = 0
            rowId = 0
            colId = 0
            for c in line:
                if c == "F":
                    rowCeil -= (rowCeil - rowFloor) / 2
                    rowId = min(int(rowCeil) - 1, int(rowFloor)) * 8
                elif c == "B":
                    rowFloor += (rowCeil - rowFloor) / 2
                    rowId = max(int(rowCeil) - 1, int(rowFloor)) * 8
                elif c == "L":
                    seatCeil -= (seatCeil - seatFloor) / 2
                    colId = min(int(seatFloor), int(seatCeil) - 1)
                elif c == "R":
                    seatFloor += (seatCeil - seatFloor) / 2
                    colId = max(int(seatFloor), int(seatCeil) - 1)
            seatIds.append(rowId + colId)
        return seatIds


partOne()
partTwo()
