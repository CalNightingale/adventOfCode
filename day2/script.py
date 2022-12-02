import pandas as pd

meToThem = {'X':'A', 'Y':'B', 'Z':'C'}
themToMe = {'A':'X', 'B':'Y', 'C':'Z'}
points = {'X': 1, 'Y': 2, 'Z': 3}
beat = {'A':'B', 'B':'C', 'C':'A'}
lose = {'A':'C', 'B':'A', 'C':'B'}

def getGameResult(them, me):
    if them == meToThem.get(me):
        return 3
    if ((them == 'A' and me == 'Y') or
        (them == 'B' and me == 'Z') or
        (them == 'C' and me == 'X')):
        return 6
    return 0

def getWhatIShouldPlay(them, res):
    if res == 'X':
        # lose
        return lose.get(them)
    elif res == 'Y':
        # draw
        return them
    else:
        # win
        return beat.get(them)

tot = 0
for them, me in pd.read_csv("data.csv", header=None, sep=' ').values:
    whatIPlay = themToMe.get(getWhatIShouldPlay(them, me))
    tot += getGameResult(them, whatIPlay) + points.get(whatIPlay)

print(tot)
