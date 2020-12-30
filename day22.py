from utils import *

DAY = day(__file__)
P1 = deque([
12,
40,
50,
4,
24,
15,
22,
43,
18,
21,
2,
42,
27,
36,
6,
31,
35,
20,
32,
1,
41,
14,
9,
44,
8])

P2 = deque([
30,
10,
47,
29,
13,
11,
49,
7,
25,
37,
33,
48,
16,
5,
45,
19,
17,
26,
46,
23,
34,
39,
28,
3,
38])

def play_game(p1,p2):
        c1=p1.popleft()
        c2=p2.popleft()
        if c1>c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

def score(winner):
    acc=0
    for i in range(1,len(winner)+1):
        acc += i*winner.pop()
    return acc

@part1
def func(expect=31809):
    p1 = P1.copy()
    p2 = P2.copy()
    while p1 and p2:
        play_game(p1, p2)
    return score(p1 or p2)

def print(*args,**kwargs):
    pass

def play_recursive_game(p1, p2, g):
    SEEN = []
    print(f"=== Game {g} ===")
    r = 0
    while p1 and p2:
        r += 1
        print(f"\n-- Round {r} (Game {g}) --")
        # block infinite recurse
        print(f"Player 1's deck: {p1}")
        print(f"Player 2's deck: {p2}")
        if ((*p1, -1, *p2)) in SEEN:
            print(f"Seen, Player 1 wins round {r} of game {g}!")
            return 1
        SEEN.append((*p1,-1,*p2))
        # each player draws a card
        c1 = p1.popleft()
        print(f"Player 1 plays: {c1}")
        c2 = p2.popleft()
        print(f"Player 2 plays: {c2}")
        # If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat
        if c1 <= len(p1) and c2 <= len(p2):
            if play_recursive_game(
                    deque(list(p1)[:c1]),
                    deque(list(p2)[:c2]),
                    g+1) == 1:
                p1.append(c1)
                p1.append(c2)
                print(f"Player 1 wins round {r} of game {g}!")
            else:
                p2.append(c2)
                p2.append(c1)
                print(f"Player 2 wins round {r} of game {g}!")

        # the winner of the round is the player with the higher-value card
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
                print(f"Player 1 wins round {r} of game {g}!")
            else:
                p2.append(c2)
                p2.append(c1)
                print(f"Player 2 wins round {r} of game {g}!")
    if g == 1:
        return score(p1 or p2)
    elif p1:
        return 1
    else:
        return 2

#P1 = deque([9, 2, 6, 3, 1])
#P2 = deque([5, 8, 4, 7, 10])

@part2
def func(expect=32835):
    p1 = P1.copy()
    p2 = P2.copy()
    return play_recursive_game(p1.copy(), p2.copy(), 1)
