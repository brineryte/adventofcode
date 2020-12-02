def partOne():
    with open("input.txt") as file:
        validCount = 0
        for line in file:
            parts = line.split(" ")
            min = int(parts[0].split("-")[0])
            max = int(parts[0].split("-")[1])
            letter = parts[1].rstrip(":")
            password = parts[2].rstrip("\n")

            if password.count(letter) >= min and password.count(letter) <= max:
                validCount += 1

    print(validCount)


def partTwo():
    with open("input.txt") as file:
        validCount = 0
        for line in file:
            parts = line.split(" ")
            pos1 = int(parts[0].split("-")[0])
            pos2 = int(parts[0].split("-")[1])
            letter = parts[1].rstrip(":")
            password = parts[2].rstrip("\n")

            if not (password[pos1-1] == letter and password[pos2-1] == letter):
                if password[pos1-1] == letter or password[pos2-1] == letter:
                    validCount += 1

    print(validCount)


partOne()
partTwo()