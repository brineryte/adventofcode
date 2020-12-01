
def partOne():
    total = 0
    with open('input2015.txt') as file:
        for line in file:
            current = line.rstrip('\n')
            dimensions = current.split('x')
            length = int(dimensions[0])
            width = int(dimensions[1])
            height = int(dimensions[2])
            total += calculatePaper(length, width, height)
    print(total)

def partTwo():
    total = 0
    with open('input2015.txt') as file:
        for line in file:
            current = line.rstrip('\n')
            dimensions = current.split('x')
            length = int(dimensions[0])
            width = int(dimensions[1])
            height = int(dimensions[2])
            total += calculateRibbon(length, width, height)
    print(total)


def calculatePaper(length, width, height):
    smallest = min(length*width, width*height, height*length)
    return 2*length*width + 2*width*height + 2*height*length + smallest


def calculateRibbon(length, width, height):
    smallest = min(2*length+2*width, 2*width+2*height, 2*height+2*length)
    return smallest + length*width*height

partOne()
partTwo()