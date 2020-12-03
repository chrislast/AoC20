from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
PARSED = [sscanf(_, r'(\d+)-(\d+) (.): (.*)', [int, int, str, str]) for _ in DATA]

@part1
def func():
    pass

@part2
def func():
    pass
