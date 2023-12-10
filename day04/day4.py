table = open(0).read().splitlines()
t = 0
a = {}
for i, l in enumerate(table):
    i += 1
    l = l.strip().split("|")
    cur = 0
    for x in l[0].split()[2:]:
        if x in l[1].split():
            cur += 1
    if str(i) in a:
        a[str(i)] += 1
    else:
        a[str(i)] = 1
    if cur:
        for j in range(i + 1, i + cur + 1):
            if str(j) in a:
                a[str(j)] += a[str(i)]
            else:
                a[str(j)] = a[str(i)]

for v in a.values():
    t += v
print(t)
