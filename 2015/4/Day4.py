import hashlib


def partOne(input):
    number = 0
    while True:
        if str(hashlib.md5(bytes(input + str(number), 'utf-8')).hexdigest())[0:5] == '00000':
            break
        number += 1

    print(number)


def partTwo(input):
    number = 0
    while True:
        if str(hashlib.md5(bytes(input + str(number), 'utf-8')).hexdigest())[0:6] == '000000':
            break
        number += 1

    print(number)


partOne('bgvyzdsv')
partTwo('bgvyzdsv')
