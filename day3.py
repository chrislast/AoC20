from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
WIDTH = len(DATA[0])
HEIGHT = len(DATA)

def f1(right=3, down=1):
    row = 0
    col = 0
    trees = 0
    while row < HEIGHT:
        if DATA[row][col] == "#":
            trees += 1
        row += down
        col = (col + right) % WIDTH
    return trees

@part1
def p1():
    return f1()

@part2
def func2():
    return f1(1,1) * f1(3,1) * f1(5,1) * f1(7,1) * f1(1,2)
