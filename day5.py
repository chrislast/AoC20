from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
SEATS = [int(_.replace("F","0").replace("B","1").replace("L","0").replace("R","1"),2) for _ in DATA]

@part1
def func(expect=938):
    return max(SEATS)

@part2
def func(expect=696):
    all = set(range(min(SEATS),max(SEATS)+1))
    return (all-set(SEATS)).pop()
