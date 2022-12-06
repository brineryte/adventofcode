with open('4.txt') as f:
    lines = f.read().splitlines()
    count = 0
    for line in lines:
        pair = line.split(',')
        first = [x for x in range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1)]
        second = [x for x in range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) + 1)]

        if set(first) <= set(second) or set(second) <= set(first):
            count += 1

    print(count)

with open('4.txt') as f:
    lines = f.read().splitlines()
    count = 0
    for line in lines:
        pair = line.split(',')
        first = [x for x in range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1)]
        second = [x for x in range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) + 1)]

        if bool(set(first) & set(second)):
            count += 1

    print(count)