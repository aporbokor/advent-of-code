import string

t = idx = 0
for line in open(0):
    prev = ""
    bc = rc = gc = 0
    for s in line.split():
        s = s.translate(str.maketrans("", "", string.punctuation))
        if prev == "Game":
            idx = int(s)
        elif s == "blue":
            bc = max(int(prev), bc)
        elif s == "red":
            rc = max(int(prev), rc)
        elif s == "green":
            gc = max(int(prev), gc)
        prev = s
    t += rc * bc * gc
print(t)
