import pandas as pd


def getStacks():
    l = pd.read_csv("start.csv", header=None)
    stacks = []
    for col in l.T.values:
        stacks.append(col.tolist())
    # stacks is a list of each column, last element is columns index
    for i, stack in enumerate(stacks):
        newstack = []
        for item in stack:
            if not item.isspace():
                newstack.append(item.strip("[] "))
        stacks[i] = newstack[:-1]
        stacks[i].reverse()
    return stacks


def getDirections():
    l = pd.read_csv("data.csv")
    return l.values.tolist()


def p1():
    stacks = getStacks()
    directions = getDirections()
    for qty, orig, dest in directions:
        for i in range(qty):
            item = stacks[orig - 1].pop()
            stacks[dest - 1].append(item)

    ans = ''
    for i in range(len(stacks)):
        ans += stacks[i][-1]
    print(ans)


def p2():
    stacks = getStacks()
    directions = getDirections()
    for qty, orig, dest in directions:
        items = []
        for i in range(qty):
            items.append(stacks[orig - 1].pop())
        items.reverse()
        stacks[dest - 1].extend(items)

    ans = ''
    for i in range(len(stacks)):
        ans += stacks[i][-1]
    print(ans)

p2()
