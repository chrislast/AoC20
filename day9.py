from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

@part1
def func(expect=1309761972):
    parsed = []
    preamble_len = 25
    for _ in DATA:
        val = int(_)
        parsed.append(val)
        if len(parsed) > preamble_len:
            valid = [
                parsed[x]+parsed[y]
                for x in range(-preamble_len-1, -1)
                for y in range(-preamble_len-1, -1)
                if x!=y]
            if val not in valid:
                return val

@part2
def func(expect=177989832):
    parsed = [int(_) for _ in DATA]
    target = 1309761972 # from part1 result
    while True:
        acc = idx = 0
        while acc < target:
            acc += parsed[idx]
            idx += 1
        if acc==target:
            found = parsed[:idx]
            assert sum(found) == target
            return min(found) + max(found)
        parsed = parsed[1:]
