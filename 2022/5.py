with open('5.txt') as f:
    lines = f.read().splitlines()

rows = []
for line in lines[0:8]:
    rows.append([line[i:i + 3] for i in range(0, len(line), 4)])

stacks = []
for item in rows[0]:
    stacks.append([])

for row in rows[::-1]:
    for i, item in enumerate(row):
        if not item.isspace():
            stacks[i].append(item)

instructions = lines[10:]

for instruction in instructions:
    pieces = instruction.split(' ')
    qty = int(pieces[1])
    source = int(pieces[3]) - 1
    dest = int(pieces[5]) - 1

    for i in range(0, qty):
        x = stacks[source].pop()
        stacks[dest].append(x)

for stack in stacks:
    print(str(stack.pop()).replace('[', '').replace(']', ''), end='')

#  PART TWO -----------------------------------------------------------
with open('5.txt') as f:
    lines = f.read().splitlines()

rows = []
for line in lines[0:8]:
    rows.append([line[i:i + 3] for i in range(0, len(line), 4)])

stacks2 = []
for item in rows[0]:
    stacks2.append([])

for row in rows[::-1]:
    for i, item in enumerate(row):
        if not item.isspace():
            stacks2[i].append(item)

instructions = lines[10:]

for instruction in instructions:
    pieces = instruction.split(' ')
    qty = int(pieces[1])
    source = int(pieces[3]) - 1
    dest = int(pieces[5]) - 1
    temp = []
    for i in range(0, qty):
        x = stacks2[source].pop()
        temp.append(x)
    temp.reverse()
    stacks2[dest] = stacks2[dest] + temp

print()
for stack in stacks2:
    print(str(stack.pop()).replace('[', '').replace(']', ''), end='')
