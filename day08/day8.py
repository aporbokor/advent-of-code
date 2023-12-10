import math

mp = open(0).read().splitlines()
moves = mp[0]
d = {}

for line in mp[2:]:
    start, opts = [x.strip() for x in (line.split("="))]
    opts = opts.split(",")
    l = opts[0][1:].strip()
    r = opts[1][: len(opts[1]) - 1].strip()
    d[start] = (l, r)


def p1():
    i = 0
    pos = "AAA"
    while True:
        if pos[-1] == "Z":
            print(i)
            break
        if moves[i % len(moves)] == "L":
            pos = d[pos][0]
        else:
            pos = d[pos][1]
        i += 1


def p2():
    start = []
    for key in d.keys():
        if key[-1] == "A":
            start.append(key)

    def f(x):
        i = 0
        while True:
            if x[-1] == "Z":
                return i
            if moves[i % len(moves)] == "L":
                x = d[x][0]
            else:
                x = d[x][1]
            i += 1

    print(math.lcm(*[f(x) for x in start]))
