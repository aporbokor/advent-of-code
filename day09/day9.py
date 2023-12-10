I = open(0).read().splitlines()
history = []
for l in I:
    history.append(list(map(int, l.split())))

t = 0
for l in history:
    cur = l
    diff = []
    a = [l]
    while not all(_ == 0 for _ in cur):
        for i in range(len(cur) - 1):
            diff.append(cur[i + 1] - cur[i])
        cur = diff[:]
        a.append(cur)
        diff.clear()
    n = 0
    a.reverse()
    for i in range(len(a) - 1):
        n = n + a[i + 1][-1]  # n = a[i + 1][0] - n for part 2
    t += n
print(t)
