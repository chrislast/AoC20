from utils import *

DAY = day(__file__)
DATA = get_input(DAY)
RULES = [_ for _ in DATA if ':' in _]
MESSAGES = [_ for _ in DATA if _ and ('a' == _[0] or 'b' == _[0])]

# "92: 26 39 | 110 18" => "p92":"({p26}{p39}|{p110}{p18})"
LOOKUP={}
for rule in RULES:
    key,expr = rule.split(":")
    if '"' in expr:
        LOOKUP[f"p{key}"] = expr[2]
    else:
        terms = expr.split("|")
        for i,term in enumerate(terms):
            terms[i] = "".join([f"{{p{_}}}" for _ in term.split()])
        LOOKUP[f"p{key}"] = f"({'|'.join(terms)})"
# pprint(LOOKUP)

def regexes():
    REGEXES={}
    breakout = max(map(len,MESSAGES))/2
    for key, regex in LOOKUP.items():
        loop=0
        while "{" in regex:
            regex = regex.format(**LOOKUP)
            loop += 1
            if loop > breakout:
                break
        REGEXES[key] = regex
    # pprint(REGEXES)
    return REGEXES

def p0():
    acc=0
    p0 = regexes()["p0"]
    for m in MESSAGES:
        if re.match(p0 + "$", m):
            acc += 1
    return acc

@part1
def func(expect=233):
    return p0()

LOOKUP["p8"] = '({p42}|{p42}{p8})'
LOOKUP["p11"] = '({p42}{p31}|{p42}{p11}{p31})'

@part2
def func(expect=396):
    return p0()

