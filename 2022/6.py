def getMessageMarker(length):
    with open('6.txt') as f:
        stream = f.read()

    n = length

    for i, item in enumerate(stream[:len(stream) - (n - 1)]):
        block = set(stream[i:i + n])
        if len(block) == n:
            return i + n, block


print(getMessageMarker(4))
print(getMessageMarker(14))
