a = []
d = {}
t = 0
for line in open(0):
    a.append(line.strip())


def solve(ri, ci, l):
    rows = [x for x in range(ri - 1, ri + 2) if x >= 0 and x < len(a)]
    cols = [x for x in range(ci - 1, ci + l + 1) if x >= 0 and x < len(a[0])]
    # print(rows)
    # print(cols)
    for r in rows:
        for c in cols:
            if a[r][c].isdigit():
                continue
            if a[r][c] == "*":
                return (r, c)
    return (-1, -1)


for r in range(len(a)):
    x, y = -1, -1
    s = ""
    for c in range(len(a[0])):
        if a[r][c].isdigit():
            if (x, y) == (-1, -1):
                x = r
                y = c
            s += a[r][c]
            if c == len(a[0]) - 1:
                if len(s) == 0:
                    continue
                z, w = solve(x, y, len(s))
                if (z, w) != (-1, -1):
                    if str(z) + " " + str(w) in d:
                        d[str(z) + " " + str(w)].append(int(s))
                    else:
                        d[str(z) + " " + str(w)] = [int(s)]
                x, y = -1, -1
                s = ""
        else:
            if len(s) == 0:
                continue
            # print("checking, ", s)
            # if solve(x, y, len(s)) != (-1, -1):
            z, w = solve(x, y, len(s))
            if (z, w) != (-1, -1):
                if str(z) + " " + str(w) in d:
                    d[str(z) + " " + str(w)].append(int(s))
                else:
                    d[str(z) + " " + str(w)] = [int(s)]

            x, y = -1, -1
            s = ""

for k in d.keys():
    # print(k, d[k])
    if len(d[k]) == 2:
        t += d[k][0] * d[k][1]

# t += 290 * 891
print(t)
