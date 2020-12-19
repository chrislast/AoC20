from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

def e(t):
    tokens = t.replace("(","").replace(")","").split()
    acc = 0
    op = "+"
    for token in tokens:
        if token in '+*':
            op = token
        elif op == "+":
            acc += int(token)
        elif op == "*":
            acc *= int(token)
    return str(acc)

@part1
def func(expect=75592527415659):
    acc = 0
    for t in DATA:
        # Brackets Out
        while True:
            m = re.search(r"(\([^()]*\))", t)
            if not m:
                # evaluate sum
                break

            else:
                # replace bracketed sum with evaluated bracket result
                t = t.replace(m.group(1), e(m.group(1)), 1)
                #print(t)
        acc += int(e(t))
    return acc

def e2(t):
    while True:
        m = re.search(r"(\d+ \+ \d+)", t)
        if not m:
            break
        else:
            # replace plus sum with result
            t = t.replace(m.group(1), e(m.group(1)), 1)
            #print(t)
    return e(t)


@part2
def func(expect=360029542265462):
    acc = 0
    for t in DATA:
        #print(f"************\n{t}")
        # Brackets Out
        while True:
            m = re.search(r"(\([^()]*\))", t)
            if not m:
                # evaluate sum
                break
            else:
                # replace bracketed sum with evaluated bracket result
                t = t.replace(m.group(1), e2(m.group(1)), 1)
                #print(t)
        ans = e2(t)
        #print(ans)
        acc += int(ans)
    return acc
