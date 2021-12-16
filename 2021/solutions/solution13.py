dirSize = 12
counts = []


def fold(paper, axis, line):
    if axis == 'y':
        foldedPaper = []
        for row in range(len(paper) - 1, line, -1):
            flippedRow = []
            for point in range(len(paper[0])):
                flippedRow.append(paper[row][point])
            foldedPaper.append(flippedRow)
        for row in range(len(foldedPaper)):
            for point in range(len(foldedPaper[0])):
                if foldedPaper[row][point] == '#':
                    paper[row][point] = '#'
        return paper[:line]
    elif axis == 'x':
        foldedPaper = []
        for row in range(len(paper)):
            flippedCol = []
            for point in range(len(paper[0]) - 1, line, -1):
                flippedCol.append(paper[row][point])
            foldedPaper.append(flippedCol)
        for row in range(len(foldedPaper)):
            for point in range(len(foldedPaper[0])):
                if foldedPaper[row][point] == '#':
                    paper[row][point] = '#'
        return [x[:line] for x in paper]


def printPaper(paper):
    count = 0
    for row in paper:
        count += row.count('#')
        print(''.join(row))
    print()
    print("dots =", count)
    counts.append(count)


with open('../inputs/input13.txt') as f:
    data = f.read().splitlines()
    data.remove('')
    directions = data[-dirSize:]
    coords = data[:-dirSize]
    width = max([max([int(x.split(',')[0])]) for x in coords]) + 1
    height = max([max([int(x.split(',')[1])]) for x in coords]) + 1

    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            point = '.'
            if str(f'{j},{i}') in coords:
                point = '#'
            row.append(point)
        grid.append(row)

    for i in directions:
        axis = 'x' if 'x' in i else 'y'
        line = i.split('=')[1]
        grid = fold(grid, axis, int(line))
        printPaper(grid)

    print(counts)
