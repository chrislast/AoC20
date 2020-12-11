from utils import *
from copy import deepcopy

DAY = day(__file__)
DATA = get_input(DAY)
EMPTY_SEAT=1
FLOOR=0
OCCUPIED=2
MAP2NUM = {".":FLOOR,"L":EMPTY_SEAT}
NUM2MAP = {FLOOR:" ", EMPTY_SEAT:"L", OCCUPIED:"*"}
PARSED = [[MAP2NUM[c] for c in l] for l in DATA]

def rule1(array, r, c):
    acc = 0
    for row in (r-1,r,r+1):
        for col in (c-1,c,c+1):
            if (r,c) != (row, col) and row>=0 and col>=0:
                try:
                    if array[row][col] is OCCUPIED:
                        acc += 1
                except:
                    pass
    return acc

def rule2(array, r, c):
    acc = 0
    for h,v in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        xpos=c
        ypos=r
        try:
            while True:
                xpos += h
                ypos += v
                if xpos<0 or ypos<0 or array[ypos][xpos] is EMPTY_SEAT:
                    break
                if array[ypos][xpos] is OCCUPIED:
                    acc+=1
                    break
        except:
            pass
    return acc

def show(arr, c):
    print(f"\n****** #{c} ******\n")
    for row in arr:
        print(''.join([NUM2MAP[i] for i in row]))

def fill_boat(rule, tolerate):
    before = None
    after = deepcopy(PARSED)
    c = 0
    while before != after:
        # show(after, c)
        # TRACE()
        before = deepcopy(after)
        for row, line in enumerate(before):
            for col, pos in enumerate(line):
                if pos is OCCUPIED:
                    if rule(before, row, col) >= tolerate:
                        after[row][col] = EMPTY_SEAT
                elif pos is EMPTY_SEAT:
                    if rule(before, row, col) == 0:
                        after[row][col] = OCCUPIED
        c += 1
    return c, after

def count_occupied(array):
    acc = 0
    for r in array:
        for c in r:
            if c is OCCUPIED:
                acc += 1
    return acc

@part1
def func(expect=2361):
    c, after = fill_boat(rule1, tolerate=4)
    show(after, c)
    return count_occupied(after)

@part2
def func(expect=2119):
    c, after = fill_boat(rule2, tolerate=5)
    show(after, c)
    return count_occupied(after)
