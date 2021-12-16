# CHEATED!!!!! by referencing someone else's solution for this one (bcuz me dumb!)
# https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_12/day_12_p2.py

from collections import defaultdict

visited = set()
visited2 = defaultdict(int)
caves = defaultdict(list)

with open('../inputs/input12.txt') as f:
    data = f.read().strip().splitlines()
    data = [i.split("-") for i in data]

    for a, b in data:
        caves[a].append(b)
        caves[b].append(a)

count = 0
count2 = 0


def searchCaves(cave):
    global count
    if cave == 'end':
        count += 1
        return

    if cave.islower() and cave in visited:
        return

    if cave.islower():
        visited.add(cave)

    for neighbor in caves[cave]:
        if neighbor != "start":
            searchCaves(neighbor)

    if cave.islower():
        visited.remove(cave)


def searchCaves2(cave):
    global count2

    if cave == 'end':
        count2 += 1
        return

    if cave.islower():
        visited2[cave] += 1

        mto = 0
        for smallCave in visited2:
            mto += visited2[smallCave] > 1

            if visited2[smallCave] > 2:
                visited2[cave] -= 1
                return

        if mto > 1:
            visited2[cave] -= 1
            return

    for neighbor in caves[cave]:
        if neighbor != "start":
            searchCaves2(neighbor)

    if cave.islower():
        visited2[cave] -= 1


searchCaves("start")
print(count)

searchCaves2("start")
print(count2)
