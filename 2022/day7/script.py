THRESHOLD = 100000
DISK_SIZE = 70000000
SPACE_FOR_UPDATE = 30000000

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

    def addChild(self, child):
        self.children.append(child)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def recurseDirSize(dir, answerList):
    size = 0
    for child in dir.children:
        if isinstance(child, File):
            # file
            size += child.size
        else:
            # subdirectory
            size += recurseDirSize(child, answerList)
    if size < THRESHOLD:
        answerList.append(size)
    dir.size = size
    return size

def getAllDirSizes(dir, dirList):
    dirList.append(dir.size)
    for child in dir.children:
        if isinstance(child, File):
            continue
        getAllDirSizes(child, dirList)

def p1():
    with open("data.txt") as file:
        lines = file.readlines()

    curDir = None
    for line in lines:
        line = line.strip('\n')
        # handle directory changing
        if line[0:4] == '$ cd':
            dirname = line.split('cd ')[1]
            if dirname != '..':
                # create a new directory
                newDir = Directory(dirname, curDir)

                if curDir:
                    curDir.addChild(newDir)

                curDir = newDir
            else:
                if curDir:
                    curDir = curDir.parent
                    
            continue

        # skip ls commands
        if line[0:4] == '$ ls':
            continue

        # skip dir listings (will be handled by $ cd logic)
        if line[0:3] == 'dir':
            continue

        # parse size and name, add to child
        size, name = line.split(' ')[:2]
        newFile = File(name, int(size))
        if curDir:
            curDir.addChild(newFile)

    # return to top of tree
    if curDir:
        while curDir.parent:
            curDir = curDir.parent

    answerList = []
    recurseDirSize(curDir, answerList)
    print(sum(answerList))

def p2():
    with open("data.txt") as file:
        lines = file.readlines()

    curDir = None
    for line in lines:
        line = line.strip('\n')
        # handle directory changing
        if line[0:4] == '$ cd':
            dirname = line.split('cd ')[1]
            if dirname != '..':
                # create a new directory
                newDir = Directory(dirname, curDir)

                if curDir:
                    curDir.addChild(newDir)

                curDir = newDir
            else:
                if curDir:
                    curDir = curDir.parent
                    
            continue

        # skip ls commands
        if line[0:4] == '$ ls':
            continue

        # skip dir listings (will be handled by $ cd logic)
        if line[0:3] == 'dir':
            continue

        # parse size and name, add to child
        size, name = line.split(' ')[:2]
        newFile = File(name, int(size))
        if curDir:
            curDir.addChild(newFile)

    if not curDir:
        return

    # return to top of tree
    while curDir.parent:
        curDir = curDir.parent


    dirSizes = []
    recurseDirSize(curDir, [])
    getAllDirSizes(curDir, dirSizes)
    availableSpace = DISK_SIZE - curDir.size
    minSpaceToFree = SPACE_FOR_UPDATE - availableSpace
    bestSize = DISK_SIZE
    for size in dirSizes:
        if size < bestSize and size > minSpaceToFree:
            bestSize = size

    print(bestSize)

p2()
