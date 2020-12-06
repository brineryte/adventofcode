from collections import Counter


def partOne():
    with open("input.txt") as file:
        myList = file.read().split("\n\n")
        total = 0
        for line in myList:
            mySet = set()
            line = line.replace("\n", "")
            for c in line:
                mySet.add(c)
            total += len(mySet)
    print(total)


def partTwo():
    with open("input.txt") as file:
        myList = file.read().split("\n\n")
        total = 0
        for line in myList:
            myList = list()
            par = len(line.split("\n"))
            line = line.replace("\n", "")
            for c in line:
                myList.append(c)
            countDict = Counter(myList)
            for count in countDict.values():
                if count == par:
                    total += 1
        print(total)


partOne()
partTwo()
