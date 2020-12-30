from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

CKEY = int(DATA[0])
DKEY = int(DATA[1])

S1 = S2 = 7

xCKEY = 5764801
xDKEY = 17807724

def test(subject_num):
    value = 1
    while True:
        value *= subject_num
        value %= 20201227
        yield value

def auth(subject_num, loops):
    value = 1
    for _ in range(loops):
        value *= subject_num
        value %= 20201227
    return value

@part1
def func(expect=9420461):
    cloop = 1
    val = test(S1)
    v = next(val)
    while v != CKEY:
        cloop += 1
        v = next(val)
    dloop = 1
    val = test(S2)
    v = next(val)
    while v != DKEY:
        dloop += 1
        v = next(val)
    ans = auth(DKEY,cloop)
    # assert ans == auth(CKEY,dloop)
    return ans

@part2
def func(expect=True):
    return True
