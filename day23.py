from utils import *

DAY = day(__file__)
DATA = "394618527"

xDATA = "389125467"

class CircularLinkedList:
    def __init__(self, cups=0):
        nums = list(range(1,max(cups,len(DATA))+1))
        for i, n in enumerate(DATA):
            nums[i] = int(n)
        self.ll = dict()
        self.head = nums[0]
        self.min = min(nums)
        self.max = max(nums)
        for i,n in enumerate(nums):
            self.ll[n] = nums[(i+1) % len(nums)]
        self.moves = 1

    def destination(self, cur, *exclude):
        while True:
            cur -= 1
            if cur < self.min:
                cur = self.max
            if cur not in exclude:
                return cur

    def next(self):
        self.head = self.ll[self.head]
        return self.head

    def move(self):
        #print(f"-- move {self.moves} --")
        self.moves += 1
        #print(f"cups: ({l[0]}) {' '.join(map(str,l[1:]))}")
        oldh = self.head
        c1 = self.next()
        c2 = self.next()
        c3 = self.next()
        newh = self.next()
        #print(f"pick up: {', '.join(map(str,self.taken))}")
        dest = self.destination(oldh,c1,c2,c3)
        #print(f"destination: {d}\n")
        self.ll[oldh] = newh
        _ = self.ll[dest]
        self.ll[dest] = c1
        self.ll[c3] = _

@part1
def func(expect=78569234):
    cups = CircularLinkedList()
    for _ in range(100):
        cups.move()
    cups.head = 1
    acc = ''
    for _ in range(len(DATA)):
        acc += str(cups.next())
    #print(f"-- final --\ncups: {' '.join(ans)}")
    return int(acc[:-1])

@part2
def func(expect=565615814504):
    cups = CircularLinkedList(1000000)
    for _ in range(10000000):
        end = cups.move()
    cups.head = 1
    c1 = cups.next()
    c2 = cups.next()
    return c1*c2
