""" Advent of Code 2020 """
# pylint: disable=C0114, C0115, C0116, C0103
import re
import math
from pathlib import Path
import pdb
import time

TRACE=pdb.set_trace
FAILED = PASSED = RAN = SKIPPED = 0

###########################

def day(fpth):
    n = int(Path(fpth).parts[-1][3:-3])
    print(f"####### Day {n} #######")
    return n

def get_input(day, converter=None, debug=False):
    """."""
    input_file = Path('input') / (str(day) + ".txt")
    try:
        with open(input_file) as f:
            text = list(map(str.strip, f.readlines()))
        if debug:
            print(f'INPUT_TEXT={text}'[:75] + '...]')
        if converter:
            return list(map(converter, text))
        return text
    except:
        return []


def lcm(*args):
    """find lowest common multiple of all integer arguments
    lcm(15,20,12) ==> 60
    """
    _lcm = int(args[0])
    for i in args[1:]:
        _lcm = int(_lcm*i/math.gcd(_lcm, int(i)))
    return _lcm


def sscanf(text, regex, converters=()):
    r"""
    example:
    sscanf("<x=-7, y=17, z=-11>",
           "x=(-?\d+), y=(-?\d+), z=(-?\d+)",
           [int]*3)
    ==> [-7, 17, -11]
    """
    _ = re.compile(regex)
    res = list(_.search(text).groups())
    for idx, cnv in enumerate(converters):
        res[idx] = cnv(res[idx])
    return tuple(res)


def bfs(textmap, start="@", end="o", wall="#", open=" "):
    """
    Breadth-first search a text map
    e.g.
    textmap = [list('#'*5), ['#','@','','o','#'], list('#'*5)]
    #####
    #@ o#
    #####
    """
    # create the search space graph
    graph = {}
    startpos = None
    endpos = None
    for y in range(len(textmap)):
        for x in range(len(textmap[0])):
            if textmap[y][x] != wall:
                graph[(x, y)] = []
                for dx, dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if textmap[dy][dx] != wall:
                        graph[(x, y)].append((dx, dy))
                if textmap[y][x] == start:
                    startpos = (x, y)

    # find the shortest route from start to end
    visited = set()
    queue = [[startpos]]
    idx = 0

    while True:
        # add the route destination to visited list
        x, y = queue[idx][-1]
        visited.add((x,y))

        # If end reached return route to end
        if textmap[y][x] == end:
            return queue[idx]

        # Add new route to queue if "edge" not already visited
        for pos in graph[(x,y)]:
            if pos not in visited:
                queue.append(queue[idx]+[pos])
        idx += 1

        # If all nodes filled return final node route
        if idx == len(queue):
            return queue[-1]

def show_part(func, part):
    global FAILED, PASSED, RAN, SKIPPED
    t1 = time.time()
    ret = func()
    elapsed = time.time()-t1
    if ret is None:
        SKIPPED += 1
        return
    RAN += 1
    expect = None
    try:
        expect = func.__defaults__[0]
    except TypeError:
        pass
    if expect:
        if ret == expect:
            print(f"\n    Part {part}\n    PASS: {ret}\n    in {elapsed:.3f} seconds")
            PASSED += 1
        else:
            print(f"\n    Part {part}\n    FAIL: {ret} expected {expect}")
            FAILED += 1
    else:
        print(f"\n    Part {part}\n    {ret}\n    in {elapsed:.3f} seconds")
    if part==2:
        print("")

def part1(func):
    show_part(func, 1)

def part2(func):
    show_part(func, 2)

class Instruction:
    def __init__(self, instruction):
        self.mnemonic, *self.oplist = instruction.split()
        self.reached = 0

class Computer:
    def __init__(self, program=None):
        self.data = []
        self.load(program)
        self.reset()

        self.instructions = dict(
            acc=self.acc,
            jmp=self.jmp,
            nop=self.nop,
            )


    def load(self, program):
        """
        Fill code memory
        """
        if program:
            self.code = [Instruction(_) for _ in program]
        else:
            self.code = []

    def dump(self):
        """
        Dump code memory
        [      0] jmp +232                 visited 1 times
        [      1] acc +21                  visited 0 times
        '''
        [    119] acc -16                  visited 0 times
        [    120] acc +45                  visited 0 times
        [    121] jmp +373                 visited 0 times
        [*   122] jmp +116                 visited 2 times
        [    123] jmp +245                 visited 0 times
        [    124] acc -19                  visited 0 times
        [    125] acc +32                  visited 0 times
        [    126] jmp -22                  visited 0 times
        """
        for idx, i in enumerate(self.code):
            here = {True:"*", False:" "}[idx==self.pc]
            print(f"[{here}{idx:-6d}] {i.mnemonic} {' '.join(i.oplist):20s} visited {i.reached} times")

    def reset(self):
        """
        Reset computer
        """
        self.pc = 0
        for i in self.code:
            i.reached = 0
        self.state = "STOPPED"
        self.registers = dict(
            acc=0
        )

    def run(self, *, reset=True, breakpoint=None, trace=False):
        """
        Run (or continue) execution until breakpoint or end reached
        """
        if reset:
            self.reset()
        self.state = "RUNNING"
        while True:
            try:
                # fetch next instruction
                i = self.code[self.pc]

            except IndexError:
                # program is complete when PC leaves code address space
                self.state = "COMPLETE"
                break

            # update profiler counter
            i.reached += 1

            # stop if breakpoint present and True
            if breakpoint and breakpoint():
                self.state = "STOPPED"
                return

            # show next line to execute
            if trace:
                print(f"[{self.pc:-6d}] {i.mnemonic} {' '.join(i.oplist):20s} {self.registers}")

            # execute instruction
            pc = self.pc
            self.instructions[i.mnemonic](i.oplist)
            # Step program counter if not changed by instruction - could break if conditional jump to self with side effect becomes a thing...
            if pc == self.pc:
                self.pc += 1

    # **** INSTRUCTION SET ****

    def nop(self, oplist):
        "No-op"
        pass

    def acc(self, oplist):
        """update acc register"""
        val = int(oplist[0])
        self.registers["acc"] += val

    def jmp(self, oplist):
        """jump"""
        val = int(oplist[0])
        self.pc += val

