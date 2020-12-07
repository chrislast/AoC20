from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
PARSED = [sscanf(_, r'(\D+ \D+) bags contain (.*)') for _ in DATA]

class Bag:
    def __init__(self, color, contents):
        self.color = color
        self.parents = list()
        self.children = dict()
        if contents != "no other bags.":
            for container in contents.split(", "):
                matched = re.match(r'(\d+) (\D+ \D+) bags?', container)
                self.children[matched.group(2)] = int(matched.group(1))

class Bags:
    def __init__(self):
        self.bags = {col:Bag(col,cont) for col, cont in PARSED}
        for col, bag in self.bags.items():
            for child in bag.children:
                self.bags[child].parents.append(bag.color)

@part1
def func(expect=261):
    bags = Bags()
    def f(bagname):
        bag = bags.bags[bagname]
        l = []
        for p in bag.parents:
            l.append(p)
            for pp in f(p):
                l.append(pp)
        return l
    return len(set(f("shiny gold")))

@part2
def func(expect=3765):
    bags = Bags()
    def f(bagname):
        bag = bags.bags[bagname]
        return sum([num + num * f(child) for child, num in bag.children.items()])
    return f("shiny gold")
