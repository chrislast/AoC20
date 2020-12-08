from utils import *

DAY = day(__file__)
PROGRAM = get_input(DAY)

COMPUTER = Computer(PROGRAM)

def breakpoint():
    """break if statement reached twice"""
    return COMPUTER.code[COMPUTER.pc].reached > 1

@part1
def func(expect=1528):
    COMPUTER.run(breakpoint=breakpoint)
    return COMPUTER.registers["acc"]

@part2
def func(expect=640):
    for i in COMPUTER.code:

        # change a nop to jmp
        if i.mnemonic == "nop":
            i.mnemonic = "jmp"
            # see if it completes
            COMPUTER.run(breakpoint=breakpoint)
            if COMPUTER.state == "COMPLETE":
                return COMPUTER.registers["acc"]
            # undo change
            i.mnemonic = "nop"

        # change a jmp to nop
        elif i.mnemonic == "jmp":
            i.mnemonic = "nop"
            # see if it completes
            COMPUTER.run(breakpoint=breakpoint)
            if COMPUTER.state == "COMPLETE":
                return COMPUTER.registers["acc"]
            # undo change
            i.mnemonic = "jmp"
