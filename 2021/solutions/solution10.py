with open('../inputs/input10.txt') as f:
    data = f.read().splitlines()

    openBraces = ['[', '{', '(', '<']
    closedBraces = [']', '}', ')', '>']
    points = [57, 1197, 3, 25137]

    scores = []
    closings = []
    for line in data:
        stack = []
        for i, char in enumerate(line):
            if char in closedBraces:
                if stack.pop() != openBraces[closedBraces.index(char)]:
                    scores.append(points[closedBraces.index(char)])
                    stack = []
                    break
            else:
                stack.append(char)
        closings.append([closedBraces[openBraces.index(x)] for x in stack[::-1]])

    print("Part One:", sum(scores))

    points = {'>': 4, '}': 3, ']': 2, ')': 1}
    scores = []
    for line in closings:
        if len(line) > 0:
            score = 0
            for char in line:
                score *= 5
                score += points[char]
            scores.append(score)

    scores.sort()
    print("Part Two:", scores[len(scores)//2])



