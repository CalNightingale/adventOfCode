def createDataMatrix(filePath):
    with open(filePath) as file:
        lines = file.readlines()

    data = []
    for line in lines:
        row = []
        line = line.strip('\n')
        for char in line:
            row.append(int(char))
        data.append(row)

    return data

def populateVisibilityMatrix(data, visiblity):
    # check horizontal visiblity
    for r in range(len(data)):
        # check from left
        curHeight = -1
        for c in range(len(data[0])):
            if data[r][c] > curHeight:
                visiblity[r][c] = True
                curHeight = data[r][c]
        # from right
        curHeight = -1
        for c in reversed(range(len(data[0]))):
            if data[r][c] > curHeight:
                visiblity[r][c] = True
                curHeight = data[r][c]

    for c in range(len(data[0])):
        # from top
        curHeight = -1
        for r in range(len(data)):
            if data[r][c] > curHeight:
                visiblity[r][c] = True
                curHeight = data[r][c]
        # from bottom
        curHeight = -1
        for r in reversed(range(len(data))):
            if data[r][c] > curHeight:
                visiblity[r][c] = True
                curHeight = data[r][c]

def getNumVisible(visiblity):
    count = 0
    for r in visiblity:
        for c in r:
            if c:
                count += 1
    return count

def computeScenicScores(data, scoreMatrix):
    bestScore = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            # trees on edges have score of 0
            if r == len(data) - 1 or r == 0 or c == len(data[0]) - 1 or c == 0:
                scoreMatrix[r][c] = 0
                continue

            curTreeHeight = data[r][c]
            # look right
            d = c + 1
            while d < len(data[0]) - 1 and data[r][d] < curTreeHeight:
                d += 1
            leftScore = d - c
            scoreMatrix[r][c] *= leftScore
            # look left
            d = c - 1
            while d > 0 and data[r][d] < curTreeHeight:
                d -= 1
            rightScore = c - d
            scoreMatrix[r][c] *= rightScore
            # look up
            d = r - 1
            while d > 0 and data[d][c] < curTreeHeight:
                d -= 1
            upScore = r - d
            scoreMatrix[r][c] *= upScore
            # look down
            d = r + 1
            while d < len(data) - 1 and data[d][c] < curTreeHeight:
                d += 1
            downScore = d - r
            scoreMatrix[r][c] *= downScore
            if scoreMatrix[r][c] > bestScore:
                bestScore = scoreMatrix[r][c]
    return bestScore




def p1():
    data = createDataMatrix("data.txt")
    visiblity = [ [False]*len(data) for _ in range(len(data[0])) ]
    populateVisibilityMatrix(data, visiblity)
    ans = getNumVisible(visiblity)
    print(ans)

def p2():
    data = createDataMatrix("data.txt")
    scoreMatrix = [ [1]*len(data) for _ in range(len(data[0])) ]
    ans = computeScenicScores(data, scoreMatrix)
    print(ans)

p2()
