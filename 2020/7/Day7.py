# --- MAIN --- #
from operator import itemgetter


def partOne(targetBag):
    with open("puzzle_input.txt") as file:
        rules = parseInputData(file)
    file.close()

    count = findAllBagsContainingTargetBag(targetBag, rules)
    print(f"Number of bags that contain at least 1 {targetBag}: {count}")


def partTwo(targetBag):
    with open("puzzle_input.txt") as file:
        rules = parseInputDataToDict(file)
    file.close()
    count = countIndividualBagsWithinBag(targetBag, rules)

    print(count)


# --- HELPERS --- #
def parseInputData(inputData):
    rules = list()
    for line in inputData:
        lineArr = line.split("contain")
        container = lineArr[0].rstrip("s ")
        contents = lineArr[1].replace("\n", "").replace(".", "").split(",")
        cleanContents(contents)
        rules.append({container: contents})
    return rules


def parseInputDataToDict(inputData):
    rules = dict()

    for line in inputData:
        lineArr = line.split("contain")
        container = lineArr[0].rstrip("s ")
        contents = lineArr[1].replace("\n", "").replace(".", "").split(",")
        cleanContents(contents)
        rules[container] = contents
    return rules


def cleanContents(contents):
    for item in range(len(contents)):
        contents[item] = contents[item].lstrip(" ")


def printRules(rules):
    for rule in rules:
        print(rule)


def findAllBagsContainingTargetBag(targetBag, rules, bagsToIgnore=None, bagCount=0):
    if bagsToIgnore is None:
        bagsToIgnore = list()
    bagCount = bagCount
    bagsToIgnore = bagsToIgnore

    for rule in rules:
        keyBag = list(rule.keys())[0]
        values = list(rule.values())[0]
        for value in values:
            if targetBag in value and keyBag not in bagsToIgnore:
                bagsToIgnore.append(keyBag)
                bagCount = 1 + findAllBagsContainingTargetBag(keyBag, rules, bagsToIgnore, bagCount)

    return bagCount


def countIndividualBagsWithinBag(targetBag, rules, count=0):
    contents = rules[targetBag]
    for item in contents:
        qty = item.split()[0]
        bagName = item.lstrip(qty + " ").rstrip("s")
        print(qty, bagName)
        if qty != 'no':
            count += int(qty) + int(qty) * countIndividualBagsWithinBag(bagName, rules)
    return count



partOne("shiny gold bag")
partTwo("shiny gold bag")
