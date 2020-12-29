from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

xDATA = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split()

def f():
    FLOOR = set()
    for line in DATA:
        line = line.replace("se","Y").replace("ne","Z").replace("sw","z").replace("nw","y").replace("e","X").replace("w","x")
        pos = (line.count("X")-line.count("x"), line.count("Y")-line.count("y"), line.count("Z")-line.count("z"))

        pos = (2 * (line.count("X") - line.count("x")) + line.count("Y") + line.count("Z") - line.count("y") - line.count("z"),
               line.count("y") + line.count("Z") - line.count("Y") - line.count("z"))
        if pos in FLOOR:
            FLOOR.remove(pos)
        else:
            FLOOR.add(pos)
    return FLOOR

@part1
def func(expect=377):
    return len(f())

@part2
def func(expect=4231):
    FLOOR = f()
    SURROUND = [(-2,0), (-1,1), (1,1), (2,0), (1,-1), (-1,-1)]
    def around(pos,floor):
        acc = 0
        for x,y in SURROUND:
            if (pos[0]+x, pos[1]+y) in floor:
                acc += 1
        return acc
    for i in range(100):
        DONE = set()
        nxt = set()
        for fx, fy in FLOOR:
            for x,y in [*SURROUND, (0,0)]:
                pos = (fx+x, fy+y)
                if pos in DONE:
                    next
                DONE.add(pos)
                blacks = around(pos,FLOOR)
                if pos in FLOOR:
                    # center is black
                    if 0 < blacks < 3:
                        nxt.add(pos)
                else:
                    if blacks == 2:
                        nxt.add(pos)
        FLOOR = nxt
        # print(f"Day {i+1}: {len(FLOOR)}")
    return len(FLOOR)
