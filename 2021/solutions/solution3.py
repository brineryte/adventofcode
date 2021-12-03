import copy
from statistics import mode

with open('../inputs/input3.txt') as f:
    data = f.read().splitlines()

    size = len(data[0])
    mask = 2 ** size - 1
    common = ''

    for bit in range(size):
        count = 0
        for i in range(len(data)):
            count += int(data[i][bit])

        common += '1' if (count > len(data)/2) else '0'


    gamma = int(common, 2)
    epsilon = ~gamma & int(bin(mask), 2)

    print(gamma, epsilon)
    print(gamma * epsilon)
    print("---------------\n")


    oxyList = data.copy()
    co2List = data.copy()
    for bit in range(size):
        currentOxyBits = [x[bit] for x in oxyList]
        currentCo2Bits = [y[bit] for y in co2List]

        currentOxyBits.sort(reverse=True)
        currentCo2Bits.sort(reverse=True)

        currentOxyBit = mode(currentOxyBits)
        currentCo2Bit = mode(currentCo2Bits)

        if len(oxyList) > 1:
            for i in range(len(oxyList)):
                if oxyList[i][bit] != currentOxyBit:
                    oxyList[i] = '.'

        if len(co2List) > 1:
            for j in range(len(co2List)):
                if co2List[j][bit] == currentCo2Bit:
                    co2List[j] = '.'

        oxyList = list(filter(lambda val: val != '.', oxyList))
        co2List = list(filter(lambda val: val != '.', co2List))

    print(oxyList, oxygen := int(oxyList[0], 2))
    print(co2List, co2 := int(co2List[0], 2))
    print(oxygen * co2)

