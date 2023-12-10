m = open(0).read().splitlines()
rs = []
rule = []
first = True


def f(mp, rs):
    n = []
    for x in rs:
        ok = 0
        for y in mp.keys():
            if x[0] in y or x[-1] in y:
                intersect = range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)
                n.append(
                    range(
                        mp[y][y.index(intersect[0])], mp[y][y.index(intersect[-1])] + 1
                    )
                )
                ok = 1
                if x == intersect:
                    break
                le = intersect[0] in x
                re = intersect[-1] in x
                if le or re:
                    if le and re:
                        lv = x[: intersect[0] - x[0]]
                        rv = x[intersect[-1] - x[0] + 1 :]
                        if len(lv) > 0:
                            n += f(mp, [lv])
                        if len(rv) > 0:
                            n += f(mp, [rv])
                    elif le:
                        lv = x[: intersect[0] - x[0]]
                        if len(lv) > 0:
                            n += f(mp, [lv])
                    else:
                        rv = x[intersect[-1] - x[0] + 1 :]
                        if len(rv) > 0:
                            n += f(mp, [rv])
                for i in n:
                    if len(i) == 0:
                        n.remove(i)
        if not ok:
            n.append(x)
    return n


def mmap(rule):
    mp = {}
    for dr, sr, rl in rule:
        mp[range(sr, sr + rl)] = range(dr, dr + rl)
    return mp


for x in m:
    if first:
        seeds = list(map(int, x.split()[1:]))
        prev = -1
        a = []
        for s in seeds:
            if prev == -1:
                prev = s
            else:
                a.append(range(prev, s + prev))
                prev = -1
        rs = a
        first = False
    elif x == "":
        if rule != []:
            rs = f(mmap(rule), rs)
        rule = []

    elif x[-1] != ":":
        rule.append(list(map(int, x.split())))
print(sorted(f(mmap(rule), rs), key=lambda r: r.start)[0][0])
