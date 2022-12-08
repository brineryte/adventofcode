def lookUp(grid, height, y, x):
    score = 0
    if y == 0:
        return True, score
    else:
        for pos in range(y-1, -1, -1):
            score += 1
            if height <= int(grid[pos][x]):
                return False, score
    return True, score


def lookDown(grid, height, y, x):
    score = 0
    if y == len(grid) - 1:
        return True, score
    else:
        for pos in range(y + 1, len(grid)):
            score += 1
            if height <= int(grid[pos][x]):
                return False, score
    return True, score


def lookLeft(grid, height, y, x):
    score = 0
    if x == 0:
        return True, score
    else:
        for pos in range(x - 1, -1, -1):
            score += 1
            if height <= int(grid[y][pos]):
                return False, score
    return True, score


def lookRight(grid, height, y, x):
    score = 0
    if x == len(grid[0]) - 1:
        return True, score
    else:
        for pos in range(x + 1, len(grid[0])):
            score += 1
            if height <= int(grid[y][pos]):
                return False, score
    return True, score


with open('8.txt') as f:
    grid = f.read().splitlines()

count = 0
scores = []
for j, y in enumerate(grid):
    for i, x in enumerate(y):
        height = int(x)
        visUp, upScore = lookUp(grid, height, j, i)
        visDown, downScore = lookDown(grid, height, j, i)
        visLeft, leftScore = lookLeft(grid, height, j, i)
        visRight, rightScore = lookRight(grid, height, j, i)
        if visUp or visDown or visLeft or visRight:
            count += 1
        scores.append(upScore * downScore * leftScore * rightScore)

print(count)
print(max(scores))




