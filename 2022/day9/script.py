class Knot:
    def __init__(self, head):
        self.x = 0
        self.y = 0
        self.head = head

    def getPos(self):
        return [self.x, self.y]

def parseInstructions(filePath):
    with open(filePath) as file:
        lines = file.readlines()

    instructions = []
    for line in lines:
        dir, mag = line.split(' ')[:2]
        instructions.append([dir, int(mag)])
    return instructions

# two positions are adjacent if they are not more than 1 unit apart in x AND y
def adjacent(k1: Knot, k2: Knot) -> bool:
    return abs(k1.x - k2.x) <= 1 and abs(k1.y - k2.y) <= 1

# dir is direction to increment head movement
def updatePos(knot: Knot, dir: str):
    # if no head, this knot is THE head. Update position directly with direction
    if knot.head == None:
        if dir == 'R':
            knot.x += 1
        elif dir == 'L':
            knot.x -= 1
        elif dir == 'U':
            knot.y += 1
        elif dir == 'D':
            knot.y -= 1
        else:
            print(f'ERROR: STRANGE DIRECTION: {dir}')
        return

    # if adjacent, no need to move tail
    if adjacent(knot, knot.head):
        return

    # adjust tail position horizontally
    if knot.x < knot.head.x:
        knot.x += 1
    elif knot.x > knot.head.x:
        knot.x -= 1
    # adjust tail position vertically
    if knot.y < knot.head.y:
        knot.y += 1
    elif knot.y > knot.head.y:
        knot.y -= 1

# position defined as x,y pair of ints
def p1():
    instructions = parseInstructions('data.txt')
    head = Knot(None)
    tail = Knot(head)
    uniquePositions = [tail.getPos()]
    for dir, mag in instructions:
        for _ in range(mag):
            updatePos(head, dir)
            updatePos(tail, '')
            tailPos = tail.getPos()
            if tailPos not in uniquePositions:
                uniquePositions.append(tailPos)
    print(len(uniquePositions))

def p2():
    instructions = parseInstructions('data.txt')
    head = Knot(None)
    m1 = Knot(head)
    m2 = Knot(m1)
    m3 = Knot(m2)
    m4 = Knot(m3)
    m5 = Knot(m4)
    m6 = Knot(m5)
    m7 = Knot(m6)
    m8 = Knot(m7)
    tail = Knot(m8)
    knots = [head, m1, m2, m3, m4, m5, m6, m7, m8, tail]
    uniquePositions = [tail.getPos()]
    for dir, mag in instructions:
        for _ in range(mag):
            for knot in knots:
                updatePos(knot, dir)
            tailPos = tail.getPos()
            if tailPos not in uniquePositions:
                uniquePositions.append(tailPos)
    print(len(uniquePositions))

p2()
