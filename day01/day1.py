t = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
a = []

def f(l, m):
    for c in l:
        if c == '\n': continue
        if c.isnumeric():
            a.clear()
            return c
        for i in range(len(a)):
            a[i] = a[i] + c
        a.append(c)
        for el in a:
            if (m):
                el = el[::-1]
            for i in range(len(digits)):
                if digits[i] == el:
                    a.clear()
                    return str(i+1)

for line in open(0):
    d1 = f(line, 0)
    line = line[::-1]
    d2 = f(line, 1)
    dig = str(d1) + str(d2)
    t += int(dig)

print(t)
