stuff = ['me', 'them', 'cool']
stuff2 = [['hey'], ['there']]


def myFunction(somelist):
    somelist[0] = '2'


def myFunction2(somelist):
    somelist[0][0] = 'yeah'


myFunction(stuff)
myFunction2(stuff2)

print(stuff)
print(stuff2)