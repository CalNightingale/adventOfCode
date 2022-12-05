import string
import pandas as pd

def p1():
    l = [i[0] for i in pd.read_csv("data.csv", header=None).values.tolist()]
    tot = 0
    for pack in l:
        print(pack)
        s = int(len(pack) / 2)
        p1 = pack[:s]
        p2 = pack[s:]
        shared = []
        for let in p1:
            if let in p2 and let not in shared:
                shared.append(let)
                val = int(string.ascii_letters.index(let)) + 1
                print(val)
                tot += val
        print(shared)
    print(tot)

def p2():
    l = [i[0] for i in pd.read_csv("data.csv", header=None).values.tolist()]
    tot = 0
    for grpnum in range(int(len(l) / 3)):
        e1 = l[grpnum*3]
        e2 = l[grpnum*3 + 1]
        e3 = l[grpnum*3 + 2]
        shared = []
        for let in e1:
            if let in e2 and let in e3 and let not in shared:
                shared.append(let)
                val = int(string.ascii_letters.index(let)) + 1
                tot += val
    print(tot)

p2()
