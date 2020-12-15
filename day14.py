from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

@part1
def func(expect=6386593869035):
    mem={}
    for row in DATA:
        inst, op = row.split(" = ")
        if inst == "mask":
            mask = op
        else:
            addr = inst[4:-1]
            val = ("0" * 35 + bin(int(op))[2:])[-36:]
            masked = [None] * 36
            for i in range(36):
                if mask[i] == "X":
                    masked[i] = val[i]
                else:
                    masked[i] = mask[i]
            mem[addr] = int(''.join(masked), 2)
    return sum(mem.values())

def all_addrs(addr, mask):
    numx = mask.count("X")
    addrbits = [_ for _ in f"{addr:036b}"]
    for i in range(36):
        if mask[i] == "X":
            addrbits[i] = "X"
        elif mask[i] == "1":
            addrbits[i] = "1"
    addrtext = ''.join(addrbits)
    addrtext = addrtext.replace("X","{}")
    acc = []
    for n in range(2**numx):
        nbin = f"{n:036b}"[-numx:]
        acc.append(int(addrtext.format(*nbin),2))
    return acc

@part2
def func(expect=4288986482164):
    mem={}
    for row in DATA:
        inst, op = row.split(" = ")
        if inst == "mask":
            mask = op
        else:
            addr = int(inst[4:-1])
            val = int(op)
            for a in all_addrs(addr, mask):
                # print(f"{a:036b} decimal({a}) <- {val}")
                mem[a] = val
    return sum(mem.values())
