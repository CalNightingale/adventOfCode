def parseInstructions(filePath):
    with open(filePath) as file:
        lines = file.readlines()

    instructions = []
    for line in lines:
        line = line.strip('\n')
        cur = []
        for part in line.split():
            try:
                cur.append(int(part))
            except:
                cur.append(part)
        instructions.append(cur)

    return instructions

def p1():
    relevant_cycles = [20,60,100,140,180,220]
    instructions = parseInstructions("data.txt")
    cycle = 0
    x = 1
    sum = 0
    for instruction in instructions:
        cycle += 1
        if cycle in relevant_cycles:
            sum += x * cycle
        if instruction[0] == 'addx':
            cycle += 1
            if cycle in relevant_cycles:
                sum += x * cycle
            x += instruction[1]

    print(sum)

def spriteIsVisible(drawLoc, spritePos):
    return abs(drawLoc - spritePos) < 2

def printSpritePos(spritePos):
    pos = ['.']*40
    pos[spritePos] = '#'
    pos[spritePos + 1] = '#'
    pos[spritePos - 1] = '#'
    res = ''
    for x in pos:
        res += x
    print(f'Sprite Position: {res}')

def p2():
    relevant_cycles = [40,80,120,160,200,240]
    instructions = parseInstructions("data.txt")
    cycle = 1
    spritePos = 1 # MIDDLE OF SPRITE
    res = ''

    def draw(res, cycle, spritePos):
        drawLoc = (cycle - 1) % 40
        toDraw = ''
        if spriteIsVisible(drawLoc, spritePos):
            toDraw += '#'
        else:
            toDraw += '.'
        if cycle in relevant_cycles:
            toDraw += '\n'
        #print(f'drawing {repr(toDraw)} in current cycle')
        res += toDraw
        #print(f'current res: {res[:39]}')
        return res

    while instructions:
        curInstruction = instructions.pop(0)
        #print(f'on cycle {cycle}, beginning execution of {curInstruction}')

        res = draw(res, cycle, spritePos)
        #printSpritePos(spritePos)

        if curInstruction[0] == 'addx':
            cycle += 1
            #print(f'mid-execution of cycle {cycle}: {curInstruction}')
            res = draw(res, cycle, spritePos)
            spritePos += curInstruction[1]

        cycle += 1

    print(res)


p2()
