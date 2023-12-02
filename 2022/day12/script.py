def parseGrid(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    grid = []
    for line in lines:
        row = []
        line = line.strip('\n')
        for c in line:
            row.append(c)
        grid.append(row)

    return grid

def getPos(grid, target):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == target:
                return (r,c)

def canMove(oldElev, newElev):
    return abs(ord(oldElev) - ord(newElev)) < 2

def recursePath(curPos, curEl, prevPos, pathLength, grid):
    print(f'At pos {curPos}. Came from {prevPos}. Length: {pathLength}')
    # end condition!
    if curEl == 'E':
        return pathLength

    bestLength = len(grid) * len(grid[0])
    # check down
    if curPos[0] < len(grid) - 1:
        newPos = (curPos[0]+1, curPos[1])
        newEl = grid[newPos[0]][newPos[1]]
        if newPos != prevPos and canMove(curEl, newEl):
            potentialLength = recursePath(newPos, newEl, curPos, pathLength + 1, grid)
            if potentialLength < bestLength:
                bestLength = potentialLength
    # check up
    if curPos[0] > 1:
        newPos = (curPos[0]-1, curPos[1])
        newEl = grid[newPos[0]][newPos[1]]
        if newPos != prevPos and canMove(curEl, newEl):
            potentialLength = recursePath(newPos, newEl, curPos, pathLength + 1, grid)
            if potentialLength < bestLength:
                bestLength = potentialLength
    # check left
    if curPos[1] > 1:
        newPos = (curPos[0], curPos[1]-1)
        newEl = grid[newPos[0]][newPos[1]]
        if newPos != prevPos and canMove(curEl, newEl):
            potentialLength = recursePath(newPos, newEl, curPos, pathLength + 1, grid)
            if potentialLength < bestLength:
                bestLength = potentialLength
    # check right
    if curPos[1] < len(grid[0]) - 1:
        newPos = (curPos[0], curPos[1]+1)
        newEl = grid[newPos[0]][newPos[1]]
        if newPos != prevPos and canMove(curEl, newEl):
            potentialLength = recursePath(newPos, newEl, curPos, pathLength + 1, grid)
            if potentialLength < bestLength:
                bestLength = potentialLength

    print(bestLength)
    return bestLength



def p1():
    grid = parseGrid("test.txt")
    print(grid)
    startPos = getPos(grid, 'S')
    ans = recursePath(startPos, 'a', [-1,-1], 0, grid)



p1()
