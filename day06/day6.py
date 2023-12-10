def p1():
    time = list(map(int, input().split()[1:]))
    dist = list(map(int, input().split()[1:]))
    td = list(zip(time, dist))
    t = 1
    for x, y in td:
        cur = 0
        for i in range(x):
            if (x - i)*i > y:
                cur += i
        t *= cur
    print(t)

def p2():
    t = int(''.join(input().split()[1:]))
    d = int(''.join(input().split()[1:]))
    l = 0
    r = t
    cur = 0
    tl = range(d)
    while (l < r):
        m = (l + r) // 2
        if (t-tl[m])*tl[m] > d:
            r = m-1
            cur = tl[m]
            print(cur)
        else:
            l = m+1
    if t % 2:
        print(abs(cur - abs(t - cur)) +1)
    else:
        print(abs(cur - abs(t - cur)))
# p1()
p2()
