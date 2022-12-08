filesys = {"/": {}}
current_dir = []
dirs = {"/": 0}


# read
def readDir(filesystem, location):
    data = filesystem
    for pos in location:
        data = data[pos]
    return data


# add
def mkDir(filesystem, location):
    data = filesystem
    for k in location:
        if k not in data.keys():
            data[k] = {}
        data = data[k]


def touch(filesystem, location, fileName, fileContent):
    data = filesystem
    lastKey = location[-1]
    for i, k in enumerate(location):
        data = data[k]
        if i == len(location) - 1:
            if ''.join(location) in dirs.keys():
                dirs[''.join(location)] += fileContent
            else:
                dirs[''.join(location)] = fileContent
            data[fileName] = fileContent


def executeCommand(line):
    global current_dir

    command = line.split(' ')[1]

    if command == "cd":
        location = line.split(' ')[2]
        if location == "..":
            if current_dir != ["/"]:
                current_dir.pop()
        else:
            current_dir.append(location)
            mkDir(filesys, current_dir)
            dirs[''.join(current_dir)] = 0



def catalogFile(line):
    touch(filesys, current_dir, line.split(' ')[1], int(line.split(' ')[0]))


def mapFileSystem():
    with open('7.txt') as f:
        lines = f.read().splitlines()

    for line in lines:
        if '$' in line:
            executeCommand(line)
        elif 'dir' not in line:
            catalogFile(line)


def sumDirectories(dirs):
    for key in dirs:
        for pos in range(0, len(key)):
            if key[0:pos] in dirs.keys():
                dirs[key[0:pos]] += dirs[key]


mapFileSystem()
sumDirectories(dirs)
print(sum([x for x in dirs.values() if x <= 100000]))
print()

print("Total space: 70000000")
print("Needed space: 30000000")
print(f"Free space: {70000000 - dirs['/']}")
print(f"Free up: {30000000 - (70000000 - dirs['/'])}")
print(min([x for x in list(dirs.values()) if x >= (30000000 - (70000000 - dirs['/']))]))
