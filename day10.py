from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
PARSED = sorted([int(_) for _ in DATA])[::-1]
PARSED.append(0)

@part1
def func(expect=1820):
    cur=device_adapter=3+max(PARSED)
    down1 = 0
    down3 = 0
    for _ in PARSED:
        if cur - _ == 3:
            down3 += 1
        elif cur - _ == 1:
            down1 += 1
        else:
            raise RuntimeError
        cur = _
    return down1 * down3

@part2
def func(expect=3454189699072):
    imax = len(PARSED)-1
    seen = [0] * len(PARSED)
    def f(i):
        if PARSED[i] == 0:
            return 1
        elif seen[i]:
            return seen[i]
        else:
            seen[i] = sum([f(_) for _ in range(i+1,i+4) if _<=imax and (PARSED[i]-PARSED[_]<=3)])
            return seen[i]
    return f(0)
