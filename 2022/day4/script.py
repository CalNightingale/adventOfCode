import pandas as pd

def p1():
    l = pd.read_csv("data.csv", header=None).values.tolist()
    tot = 0
    for p1, p2 in l:
        p1s, p1e = map(int, p1.split('-'))
        p2s, p2e = map(int, p2.split('-'))
        # overlap if p2 starts after and ends before p1, or vice versa
        if (p1s <= p2s and p1e >= p2e) or (p2s <= p1s and p2e >= p1e):
            tot += 1
    print(tot)

def p2():
    l = pd.read_csv("data.csv", header=None).values.tolist()
    tot = 0
    for p1, p2 in l:
        p1s, p1e = map(int, p1.split('-'))
        p2s, p2e = map(int, p2.split('-'))
        # check NOT overlapping
        if (p1s < p2s and p1e < p2s) or (p1s > p2e and p1e > p2e) or (p2s < p1s and p2e < p1s) or (p2s > p1e and p2e > p1e):
            continue
        tot += 1
    print(tot)

p2()
