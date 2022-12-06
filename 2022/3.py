item_priority = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i, a in enumerate(alpha):
    item_priority[a] = i + 1

for i, a in enumerate(alpha):
    item_priority[str(a).upper()] = i + 27

print(item_priority)

with open('3.txt') as f:
    sacks = f.read().splitlines()

    total = 0
    for sack in sacks:
        poc1 = sack[0:int(len(sack)/2)]
        poc2 = sack[int(len(sack)/2):]
        total += item_priority[list(set(poc1).intersection(set(poc2)))[0]]
    print(total)

with open('3.txt') as f:
    lines = f.read().splitlines()
    sets = []
    for line in lines:
        sets.append(set(line))

    groups = [sets[i:i + 3] for i in range(0, len(sets), 3)]

    total = 0
    for group in groups:
        total += item_priority[list(group[0] & group[1] & group[2])[0]]

    print(total)


