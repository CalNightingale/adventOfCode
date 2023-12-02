import operator
import math
ops = { "+": operator.add, "-": operator.sub, '*' : operator.mul, '/' : operator.truediv}

class Monkey:
    def __init__(self):
        self.id = -1
        self.items = []
        self.operation = None
        self.coeff = 0
        self.test = 0
        self.trueAction = -1
        self.falseAction = -1
        self.inspections = 0

    def __str__(self):
        return f'Monkey {self.id}:\n   Items: {self.items}\n   Op: {self.operation} {self.coeff}\n   Test: {self.test}\n   True: {self.trueAction}\n   False: {self.falseAction}'

    def inspect(self, val):
        self.inspections += 1
        if isinstance(self.coeff, int):
            return self.operation(val, self.coeff)
        return self.operation(val, val)

    def executeTest(self, val):
        return val % self.test == 0


def parseMonkeys(filePath):
    monkeys = []
    with open(filePath) as file:
        lines = file.readlines()

    id = -1
    items = []
    function = None
    test = 0
    trueAction = -1
    falseAction = -1

    curMonkey = Monkey()
    for line in lines:
        line = line.strip('\n').split()
        if not line: continue
        # new monkey: store id
        if line[0] == 'Monkey':
            id = int(line[1].split(':')[0])
            curMonkey.id = id
        # store starting items
        elif line[0] == 'Starting':
            items = [int(i.split(',')[0]) for i in line[2:]]
            curMonkey.items = items
        # store operation
        elif line[0] == 'Operation:':
            curMonkey.operation = ops[line[4]]
            try:
                curMonkey.coeff = int(line[5])
            except:
                curMonkey.coeff = line[5]
        # store test
        elif line[0] == 'Test:':
            test = int(line[3])
            curMonkey.test = test
        # store trueRecipient
        elif line[1] == 'true:':
            trueAction = int(line[5])
            curMonkey.trueAction = trueAction
        # store falseRecipient, create monkey, append
        elif line[1] == 'false:':
            falseAction = int(line[5])
            curMonkey.falseAction = falseAction
            monkeys.append(curMonkey)
            curMonkey = Monkey()
    return monkeys


def p1():
    NUM_ROUNDS = 20
    monkeys = parseMonkeys("data.txt")
    for round in range(NUM_ROUNDS):
        for monkey in monkeys:
            processedItems = []
            while monkey.items:
                curItem = monkey.items.pop(0)
                #print(f'inspecting item {curItem} belonging to monkey {monkey.id}')
                curItem = monkey.inspect(curItem)
                #print(f'new worry level: {curItem}')
                curItem = math.floor(curItem / 3)
                #print(f'after inspection: {curItem}')
                testRes = monkey.executeTest(curItem)
                #print(f'test result: {testRes}')
                monkeys[monkey.trueAction if testRes else monkey.falseAction].items.append(curItem)
                #print(f'Item with worry level {curItem} thrown to monkey {monkey.trueAction if testRes else monkey.falseAction}')
                #print()
        print(f"After round {round + 1}:")
        for monkey in monkeys:
            print(f'Monkey {monkey.id}: {monkey.items}')
        print()

    print(f'After {NUM_ROUNDS} rounds...')
    inspections = []
    for monkey in monkeys:
        print(f'Monkey {monkey.id} inspected items {monkey.inspections} times.')
        inspections.append(monkey.inspections)
                
    mostInspections = max(inspections)
    inspections.remove(mostInspections)
    secondMostInspections = max(inspections)
    print(mostInspections * secondMostInspections)

def p2():
    NUM_ROUNDS = 20
    monkeys = parseMonkeys("data.txt")
    for round in range(NUM_ROUNDS):
        for monkey in monkeys:
            processedItems = []
            while monkey.items:
                curItem = monkey.items.pop(0)
                #print(f'inspecting item {curItem} belonging to monkey {monkey.id}')
                curItem = monkey.inspect(curItem)
                #print(f'new worry level: {curItem}')
                testRes = monkey.executeTest(curItem)
                #print(f'test result: {testRes}')
                monkeys[monkey.trueAction if testRes else monkey.falseAction].items.append(curItem)
                #print(f'Item with worry level {curItem} thrown to monkey {monkey.trueAction if testRes else monkey.falseAction}')
                #print()

    print(f'After {NUM_ROUNDS} rounds...')
    inspections = []
    for monkey in monkeys:
        print(f'Monkey {monkey.id} inspected items {monkey.inspections} times.')
        inspections.append(monkey.inspections)
                
    mostInspections = max(inspections)
    inspections.remove(mostInspections)
    secondMostInspections = max(inspections)
    print(mostInspections * secondMostInspections)

p2()
