from utils import *
from collections import Counter

DAY = day(__file__)
DATA = get_input(DAY)
PARSED = [sscanf(_, r'(\d+)-(\d+) (.): (.*)', [int, int, str, str]) for _ in DATA]

@part1
def p1():
    count = 0
    for lo, hi, ch, pw in PARSED:
        if lo <= Counter(pw)[ch] <= hi:
            count += 1
    return count

@part2
def p2():
    count = 0
    for p1, p2, ch, pw in PARSED:
        if (pw[p1-1]==ch or pw[p2-1]==ch) and pw[p1-1]!=pw[p2-1]:
            count += 1
    return count
