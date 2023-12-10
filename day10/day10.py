import sys

sys.setrecursionlimit(100000000)


class Node:
    def __init__(self, v, r, c, vi=0):
        self.val = v
        self.row = r
        self.col = c
        self.vis = vi

    def __str__(self):
        return f"({self.row},{self.col})"

    def adjacentEdges(self):
        n = []
        north = ["|", "L", "J", "S"]
        south = ["|", "7", "F", "S"]
        east = ["-", "L", "F", "S"]
        west = ["-", "J", "7", "S"]
        if self.val in north and self.row > 0:  # go north
            nxt = G[self.row - 1][self.col]
            if nxt.val in south:
                n.append(nxt)
        if self.val in south and self.row < len(G) - 1:  # south
            nxt = G[self.row + 1][self.col]
            if nxt.val in north:
                n.append(nxt)
        if self.val in east and self.col < len(G[0]) - 1:  # east
            nxt = G[self.row][self.col + 1]
            if nxt.val in west:
                n.append(nxt)
        if self.val in west and self.col > 0:  # west
            nxt = G[self.row][self.col - 1]
            if nxt.val in east:
                n.append(nxt)
        return n


inp = open(0).read().splitlines()
grid = []
for r in inp:
    grid.append([*r])
G = []
root = []
for r in range(len(grid)):
    n = []
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            root = Node(grid[r][c], r, c)
        n.append(Node(grid[r][c], r, c))
    G.append(n)

def p1():
    size = 0

    def dfs(v, size):
        G[v.row][v.col].vis = True
        for w in v.adjacentEdges():
            if size > 1 and w.val == "S":
                if size % 2 == 0:
                    print(size // 2)
                else:
                    print((size + 1) // 2)
                return
            if w.val == ".":
                continue
            if not w.vis:
                dfs(w, size + 1)

    dfs(root, size)


def p2():
    # use shoelace to find area
    def dfs(v, size, path):
        G[v.row][v.col].vis = True
        path.append(v)
        for w in v.adjacentEdges():
            if size > 1 and w.val == "S":
                return path
            if w.val == ".":
                continue
            if not w.vis:
                return dfs(w, size + 1, path)


    path = dfs(root, 0, [])
    p1 = zip(path, path[1:] + [path[0]])
    p2 = zip(path, path[1:] + [path[0]])
    a = sum([x.row * y.col for x, y in p1])
    b = sum([x.col * y.row for x, y in p2])

    A = int(abs(a - b) / 2)

    # and now apply Pick's theorem (where i is the number of integer points interior to the
    # polygon, and b is the number of integer points on its boundary)
    i = A - len(path) / 2 + 1
    print(int(i))
