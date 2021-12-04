def getAllWinningCombos(board):
    combinations = board.copy()

    for num in range(len(board[0])):
        combinations.append([x[num] for x in board])

    return combinations


def findEarliestWin(nums, combinations):
    earliestWinIndex = len(nums)
    winningCombo = set()

    for index in range(len(nums)):
        setNums = set(nums[:index])
        for combo in combinations:
            setCombo = set(combo)
            if setCombo.issubset(setNums):
                earliestWinIndex = index
                winningCombo = setCombo
                return earliestWinIndex, winningCombo

    return earliestWinIndex, winningCombo


with open('../inputs/input4.txt') as f:
    data = f.read().splitlines()

    numbers = data[0].split(',')

    boardData = list(filter(lambda val: val != '', data[2:]))

    boards = []
    for i in range(0, len(boardData), 5):
        boards.append([[y for y in x.split(' ') if y] for x in boardData[i:i + 5]])

    wins = []
    winningCombos = []
    for board in boards:
        combos = getAllWinningCombos(board)
        win, winningCombo = findEarliestWin(numbers, combos)
        wins.append(win)
        winningCombos.append(winningCombo)

    winningIndex = wins.index(min(wins))
    winningNumber = numbers[min(wins)-1]
    winningBoard = boards[winningIndex]
    winningCombo = winningCombos[winningIndex]

    losingIndex = wins.index(max(wins))
    losingNumber = numbers[max(wins)-1]
    losingBoard = boards[losingIndex]
    losingCombo = winningCombos[losingIndex]

    nums = [int(x) for x in numbers[:min(wins)]]
    unmarkedNums = [[int(y) for y in x if int(y) not in nums] for x in winningBoard]
    unmarkedSum = sum([sum(x) for x in unmarkedNums])
    print("Part one:", unmarkedSum * int(winningNumber))

    nums2 = [int(x) for x in numbers[:max(wins)]]
    unmarkedNums2 = [[int(y) for y in x if int(y) not in nums2] for x in losingBoard]
    unmarkedSum2 = sum([sum(x) for x in unmarkedNums2])
    print("Part two:", unmarkedSum2 * int(losingNumber))
