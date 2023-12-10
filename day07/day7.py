import functools

cards = [line.split() for line in open(0)]
d1 = d2 = {}
for a, b in cards:
    d1[a] = int(b)


def comp(a, b):
    for i in range(5):
        if a[i] == b[i]:
            continue
        if a[i] == "J":  # comment to run p1
            return -1
        if b[i] == "J":
            return 1
        if a[i].isnumeric():
            if b[i].isnumeric():
                if int(a[i]) > int(b[i]):
                    return 1
                return -1
            else:
                return -1
        else:
            if b[i].isnumeric():
                return 1
            else:
                if d2[a[i]] > d2[b[i]]:
                    return 1
                return -1


def p1():
    global d2
    d2 = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    order = [[] for i in range(7)]
    for c, _ in cards:
        typ = list(
            set([(c.count(letter), c, letter) for letter in c if c.count(letter) > 1])
        )
        typ.sort(key=lambda x: x[0], reverse=True)
        if typ == []:
            order[0].append(c)
            continue
        match typ[0][0]:
            case 5:
                order[6].append(c)
            case 4:
                order[5].append(c)
            case 3:
                if len(typ) == 2:
                    order[4].append(c)
                else:
                    order[3].append(c)
            case 2:
                if len(typ) == 2:
                    order[2].append(c)
                else:
                    order[1].append(c)
    for l in order:
        l.sort(key=functools.cmp_to_key(comp))
    rank = 1
    t = 0
    for l in order:
        if l == []:
            continue
        for x in l:
            t += d1[x] * rank
            rank += 1
    print(t)


def p2():
    d2 = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    order = [[] for i in range(7)]
    for c, _ in cards:
        typ = list(
            set(
                [
                    (c.count(letter), c, letter)
                    for letter in c
                    if letter != "J" and c.count(letter) > 1
                ]
            )
        )
        typ.sort(key=lambda x: x[0], reverse=True)
        if typ == []:
            if c.count("J") == 0:
                order[0].append(c)
                continue
            elif c.count("J") == 5:
                rep = 5
            else:
                rep = c.count("J") + 1
        else:
            rep = typ[0][0] + c.count("J")
        match rep:
            case 5:
                order[6].append(c)
            case 4:
                order[5].append(c)
            case 3:
                if len(typ) == 2:
                    order[4].append(c)
                else:
                    order[3].append(c)
            case 2:
                if len(typ) == 2:
                    order[2].append(c)
                else:
                    order[1].append(c)
    for l in order:
        l.sort(key=functools.cmp_to_key(comp))
    rank = 1
    t = 0
    for l in order:
        if l == []:
            continue
        for x in l:
            t += d1[x] * rank
            rank += 1
    print(t)
p2()
