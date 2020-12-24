from utils import *
import numpy as np

DAY = day(__file__)
DATA = get_input(DAY)

# DATA = [
# "Tile 2311:",
# "..##.#..#.",
# "##..#.....",
# "#...##..#.",
# "####.#...#",
# "##.##.###.",
# "##...#.###",
# ".#.#.#..##",
# "..#....#..",
# "###...#.#.",
# "..###..###",
# "",
# ]

TILES = {}
JOINS = {}
ARRS = {}
try:
    i = 0
    while True:
        tile = DATA[i][5:-1]
        arr = np.array(DATA[i+1:i+11],dtype=('U1',10))
        ARRS[tile] = arr
        edges = [arr[0,:],arr[-1,:],reversed(arr[0,:]),reversed(arr[-1,:]),
                 arr[:,0],arr[:,-1],reversed(arr[:,0]),reversed(arr[:,-1])]
        TILES[tile] = set(map(lambda x:''.join(x), edges))
        for edge in TILES[tile]:
            if edge in JOINS:
                JOINS[edge].add(tile)
            else:
                JOINS[edge] = set((tile,))
        i += 12
except IndexError:
    pass

def f(key):
    acc = 0
    for edge in JOINS:
        if key in JOINS[edge] and len(JOINS[edge])==1:
            acc += 1
    return acc

NEIGHBOURS = dict()
for _ in TILES:
    for ptn in TILES[_]:
        if _ in NEIGHBOURS:
            NEIGHBOURS[_].update(JOINS[ptn])
        else:
            NEIGHBOURS[_] = JOINS[ptn].copy()
    NEIGHBOURS[_].remove(_)

CORNERS = {_:TILES[_] for _ in TILES if f(_) == 4}

EDGES = {_:TILES[_] for _ in TILES if f(_) <= 6}

FOUND = set()

@part1
def func(expect=54755174472007):
    return math.prod(map(int, CORNERS))


def orientate(arr, target, side):
    for _ in range(2):
        for __ in range(4):
            if ((side=="L" and target==''.join(arr[:,0])) or
                (side=="R" and target==''.join(arr[:,-1])) or
                (side=="U" and target==''.join(arr[0,:])) or
                (side=="D" and target==''.join(arr[-1,:]))):
                return arr
            arr = np.rot90(arr,1)
        arr = arr.transpose()
    raise RuntimeError("no match found")

def show_world(world):
    wx,wy,wz = world.shape
    ax1,ay1 = world[0,0,0].shape
    ay2 = ay1 - 2
    ax2 = ax1 - 2
    arr1 = np.zeros(shape=(wx*ax1, wy*ay1), dtype=object)
    arr2 = np.zeros(shape=(wx*ax2, wy*ay2), dtype=object)
    for x in range(wx):
        for y in range(wy):
            arr1[y*ay1:y*ay1+ay1, x*ax1:x*ax1+ax1] = world[y,x,0][:,:]
            arr2[y*ay2:y*ay2+ay2, x*ax2:x*ax2+ax2] = world[y,x,0][1:-1,1:-1]
    return arr2

def find_sea_monsters(world):
    SEA_MONSTER=np.array(
        ["..................o.",
         "o....oo....oo....ooo",
         ".o..o..o..o..o..o..."],dtype=('U1',20))
    wy,wx=world.shape
    my,mx=SEA_MONSTER.shape
    zzz = np.zeros(shape=(wy,wx), dtype=object)
    zzz.fill(".")
    loop = 0
    while loop<8:
        if loop == 4:
            world = world.transpose()
        else:
            world = np.rot90(world,1)
        acc = 0
        for x in range(wx-mx):
            for y in range(wy-my):
                if tuple((SEA_MONSTER + world[y+0:y+3,x+0:x+20]).reshape(1,60)[0]).count("o#") == 15:
                    for yy,xx in [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]:
                        world[y+yy,x+xx] = "o"
                    zzz[y:y+my,x:x+mx] = SEA_MONSTER
                    acc += 1
        if acc:
            return acc, world, zzz
        loop += 1
    raise RuntimeError("No monsters")

@part2
def func(expect=1692):
    # create an empty array
    dim = int(len(TILES)**0.5)
    world = np.zeros(shape=(dim,dim,2), dtype=object)
    # pick a corner and one of it's neighbours at random
    for corner in CORNERS:
        break
    for neigh in NEIGHBOURS[corner]:
        break
    world[0,0,0] = ARRS[corner]
    world[0,0,1] = corner
    world[1,0,0] = ARRS[neigh]
    world[1,0,1] = neigh
    for joint,pair in JOINS.items():
        if {corner, neigh} == pair:
            break

    # line up first two pieces
    world[0,0,0] = orientate(world[0,0,0], joint,"D")
    world[1,0,0] = orientate(world[1,0,0], joint,"U")

    # complete the column
    for i in range(2,dim):
        joint = ''.join(world[i-1,0,0][-1,:])  # last row
        joined = JOINS[joint]
        neigh = [_ for _ in joined if _ not in world[:,:,1]][0]
        world[i,0,0] = ARRS[neigh]
        world[i,0,1] = neigh
        world[i,0,0] = orientate(world[i,0,0], joint,"U")

    # complete the rows
    for x in range(1,dim):
        for y in range(dim):
            joint = ''.join(world[y,x-1,0][:,-1])  # last col
            joined = JOINS[joint]
            for neigh in joined:
                if neigh in world[:,:,1]:
                    continue
                break
            world[y,x,0] = ARRS[neigh]
            world[y,x,1] = neigh
            world[y,x,0] = orientate(world[y,x,0], joint,"L")

    new_world = show_world(world)
    cnt, www, zzz = find_sea_monsters(new_world)
    txt = [''.join(row) for row in www]
    worldmap = '\n'.join(txt)
    print(worldmap)
    return worldmap.count("#")
