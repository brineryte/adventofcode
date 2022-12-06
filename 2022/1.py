

with open('1.txt') as file:
    elves = file.read().split('\n\n')
    calories = []

    for elf in elves:
        total = 0
        for food in elf.splitlines():
            total += int(food)
        calories.append(total)

    print(max(calories))


# 2
with open('1.txt') as file:
    elves = file.read().split('\n\n')
    calories = []

    for elf in elves:
        total = 0
        for food in elf.splitlines():
            total += int(food)
        calories.append(total)

    calories.sort(reverse=True)
    print(sum(calories[0:3]))