from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

WORLD = {(x,y,0) for y in range(len(DATA)) for x in range(len(DATA[0])) if DATA[y][x]=="#"}

def count_neighbours(world, _x, _y, _z):
    acc = 0
    for x in range(_x-1, _x+2):
        for y in range(_y-1, _y+2):
            for z in range(_z-1, _z+2):
                if (x,y,z) != (_x,_y,_z):
                    if (x,y,z) in world:
                        acc+=1
    return acc

@part1
def func(expect=301):
    now = WORLD.copy()
    for loop in range(6):
        soon=set()
        minx=min([_[0] for _ in now])-1
        miny=min([_[1] for _ in now])-1
        minz=min([_[2] for _ in now])-1
        maxx=max([_[0] for _ in now])+1
        maxy=max([_[1] for _ in now])+1
        maxz=max([_[2] for _ in now])+1
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                for z in range(minz, maxz+1):
                    n = count_neighbours(now,x,y,z)
                    if (x,y,z) in now:
                        if n==2 or n==3:
                            soon.add((x,y,z))
                    elif n==3:
                        soon.add((x,y,z))
        now=soon
    return len(now)

WORLD = {(x,y,0,0) for y in range(len(DATA)) for x in range(len(DATA[0])) if DATA[y][x]=="#"}

def count_neighbours(world, _x, _y, _z, _w):
    acc = 0
    for x in range(_x-1, _x+2):
        for y in range(_y-1, _y+2):
            for z in range(_z-1, _z+2):
                for w in range(_w-1, _w+2):
                    if (x,y,z,w) != (_x,_y,_z,_w):
                        if (x,y,z,w) in world:
                            acc+=1
    return acc

@part2
def func(expect=2424):
    now = WORLD.copy()
    for loop in range(6):
        soon=set()
        minx=min([_[0] for _ in now])-1
        miny=min([_[1] for _ in now])-1
        minz=min([_[2] for _ in now])-1
        minw=min([_[3] for _ in now])-1
        maxx=max([_[0] for _ in now])+1
        maxy=max([_[1] for _ in now])+1
        maxz=max([_[2] for _ in now])+1
        maxw=max([_[3] for _ in now])+1
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                for z in range(minz, maxz+1):
                    for w in range(minw, maxw+1):
                        n = count_neighbours(now,x,y,z,w)
                        if (x,y,z,w) in now:
                            if n==2 or n==3:
                                soon.add((x,y,z,w))
                        elif n==3:
                            soon.add((x,y,z,w))
        now=soon
    return len(now)
