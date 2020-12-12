from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
PARSED = [sscanf(_, r'(.)(\d+)', [str, int]) for _ in DATA]

SOUTH = 180
EAST = 90
NORTH = 0
WEST = 270
VEC = {SOUTH:(0,-1),EAST:(1, 0),NORTH:(0,1),WEST:(-1, 0)}

class Ferry1:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = EAST
        self.vec = VEC[self.dir]

    def left(self, deg):
        self.dir = (self.dir + 360 - deg) % 360
        self.vec = VEC[self.dir]

    def right(self, deg):
        self.dir = (self.dir + deg) % 360
        self.vec = VEC[self.dir]

    def move(self, steps, xvec, yvec):
        self.x += xvec * steps
        self.y += yvec * steps

    def go(self, route):
        for command, steps in route:
            {
                "L": lambda: self.left(steps),
                "R": lambda: self.right(steps),
                "N": lambda: self.move(steps, *VEC[NORTH]),
                "S": lambda: self.move(steps, *VEC[SOUTH]),
                "E": lambda: self.move(steps, *VEC[EAST]),
                "W": lambda: self.move(steps, *VEC[WEST]),
                "F": lambda: self.move(steps, *self.vec),
            }[command]()
        return abs(self.x) + abs(self.y)

@part1
def func(expect=1294):
    return Ferry1().go(PARSED)

class Ferry2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = 1

    def left(self, deg):
        while deg:
            deg -= 90
            self.wx, self.wy = -self.wy, self.wx

    def right(self, deg):
        while deg:
            deg -= 90
            self.wx, self.wy = self.wy, -self.wx

    def wmove(self, x, y):
        self.wx += x
        self.wy += y

    def move(self, steps):
        self.x += self.wx * steps
        self.y += self.wy * steps

    def go(self, route):
        for command, steps in route:
            {
                "L": lambda: self.left(steps),
                "R": lambda: self.right(steps),
                "N": lambda: self.wmove(0, steps),
                "S": lambda: self.wmove(0, -steps),
                "E": lambda: self.wmove(steps, 0),
                "W": lambda: self.wmove(-steps, 0),
                "F": lambda: self.move(steps),
            }[command]()
        return abs(self.x) + abs(self.y)

@part2
def func(expect=20592):
    return Ferry2().go(PARSED)
