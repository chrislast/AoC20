from utils import get_input

DATA = get_input(1, int) # 200 items

def part1():
    return [x*y for x in DATA for y in DATA if x+y==2020 and x!=y][0] # 40K loops

def part2():
    def func():
        loopc=0
        for ix, x in enumerate(DATA):
            for iy, y in enumerate(DATA[ix+1:]):
                if x + y < 2020:
                    for z in DATA[ix+iy+2:]:
                        loopc+=1
                        if x+y+z==2020:
                            yield x*y*z  #, x, y, z, loopc
    return next(func()) # much faster - 20K loops not 8M
    # return [x*y*z for x in DATA for y in DATA for z in DATA if x+y+z==2020 and x!=y and x!=z and y!=z][0]

if __name__ == "__main__":
    print(f"\n    Part 1\n    {part1()}")
    print(f"\n    Part 2\n    {part2()}")
