from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

@part1
def func(expect=1528):
    c=Computer()
    c.load(DATA)
    def breakpoint():
        return c.code[c.pc].reached > 1
    c.run(breakpoint=breakpoint)
    return c.registers["acc"]

@part2
def func(expect=640):
    c=Computer()
    c.load(DATA)
    def breakpoint():
        return c.code[c.pc].reached > 1
    for i in c.code:
        if i.mnemonic == "nop":
            i.mnemonic = "jmp"
            c.run(breakpoint=breakpoint)
            if c.state == "COMPLETE":
                return c.registers["acc"]
            i.mnemonic = "nop"

        elif i.mnemonic == "jmp":
            i.mnemonic = "nop"
            c.run(breakpoint=breakpoint)
            if c.state == "COMPLETE":
                return c.registers["acc"]
            i.mnemonic = "jmp"
