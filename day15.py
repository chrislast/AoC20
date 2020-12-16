from utils import *

DAY = day(__file__)
MEM = {
20: [1, None],
0:  [2, None],
1:  [3, None],
11: [4, None],
6:  [5, None],
3:  [6, None],
}

@part1
def func(expect=421):
    turn = len(MEM)+1
    last = list(MEM.keys())[-1]
    while turn <= 2020:
        t1,t2 = MEM[last]
        if t2 is None:
            this = 0
        else:
            this = t1 - t2
        if this in MEM:
            MEM[this][1] = MEM[this][0]
            MEM[this][0] = turn
        else:
            MEM.update({this:[turn, None]})
        last = this
        turn += 1
    return last

MEM = {
20: [1, None],
0:  [2, None],
1:  [3, None],
11: [4, None],
6:  [5, None],
3:  [6, None],
}

@part2
def func(expect=436):
    turn = len(MEM)+1
    last = list(MEM.keys())[-1]
    while turn <= 30000000:
        t1,t2 = MEM[last]
        if t2 is None:
            this = 0
        else:
            this = t1 - t2
        if this in MEM:
            MEM[this][1] = MEM[this][0]
            MEM[this][0] = turn
        else:
            MEM.update({this:[turn, None]})
        last = this
        turn += 1
    return last

