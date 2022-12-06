win = ['AY', 'BZ', 'CX']
draw = ['AX', 'BY', 'CZ']

with open('2.txt') as f:
    rounds = [x.replace(' ', '') for x in f.read().splitlines()]

    total = 0
    for r in rounds:
        score = 0
        if r in win:
            score += 6
        elif r in draw:
            score += 3

        if 'X' in r:
            score += 1
        elif 'Y' in r:
            score += 2
        elif 'Z' in r:
            score += 3

        total += score
    print(total)

values = {'A': 1, 'B': 2, 'C': 3}
win2 = {'A': 'B', 'B': 'C', 'C': 'A'}
draw2 = {'A': 'A', 'B': 'B', 'C': 'C'}
lose2 = {'A': 'C', 'B': 'A', 'C': 'B'}
lose, draw, win = 'X', 'Y', 'Z'

with open('2.txt') as f:
    rounds = [x.replace(' ', '') for x in f.read().splitlines()]

    total2 = 0
    for r in rounds:
        score = 0
        shape = r[0]
        outcome = r[1]

        if outcome == lose:
            score += 0
            score += values[lose2[r[0]]]
        elif outcome == draw:
            score += 3
            score += values[draw2[r[0]]]
        else:
            score += 6
            score += values[win2[r[0]]]

        total2 += score


    print(total2)
