from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

@part1
def func(expect=6726):
    groups = []
    groups.append(set())
    for line in DATA:
        if not line:
            groups.append(set())
        else:

            for yes in line:
                groups[-1].add(yes)
    return sum(map(len, groups))

@part2
def func(expect=3316):
    groups = []
    l=0
    groups.append(set())
    for line in DATA:
        if not line:
            groups.append(set())
            l=0
        else:
            answers = {_ for _ in line}
            if l == 0:
                groups[-1] = answers
            else:
                groups[-1] &= answers
            l+=1
    return sum(map(len, groups))
