

def checkUnique(l):
    for c in l:
        if l.count(c) > 1:
            return False
    return True


def p1():
    data = None
    with open("data.txt") as file:
        data = file.read()
    last4 = []
    cur = None
    for i, c in enumerate(data):
        cur = i
        print(c)
        if i < 5:
            last4.append(c)
            if i == 4 and checkUnique(last4):
                break
            continue

        # append new, remove old (now 5th), check uniqueness
        last4.append(c)
        last4.pop(0)
        if checkUnique(last4):
            break

def p2():
    data = None
    with open("data.txt") as file:
        data = file.read()
    last14 = []
    cur = None
    for i, c in enumerate(data):
        cur = i
        if i < 14:
            last14.append(c)
            if i == 13 and checkUnique(last14):
                break
            continue

        # append new, remove old (now 15th), check uniqueness
        last14.append(c)
        last14.pop(0)
        if checkUnique(last14):
            break
    cur += 1 # handle 1-indexing
    print(cur)

p2()

