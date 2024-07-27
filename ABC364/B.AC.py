H, W = map(int, input().split())
Si, Sj = map(int, input().split())

G = []

for i in range(H):
    g = input()
    G.append(g)

X = input()

c = [Si - 1, Sj - 1]
for x in X:
    if x == "L":
        if c[1] == 0:
            continue
        if G[c[0]][c[1] - 1] == "#":
            continue
        c[1] -= 1
    if x == "R":
        if c[1] == W - 1:
            continue
        if G[c[0]][c[1] + 1] == "#":
            continue
        c[1] += 1
    if x == "U":
        if c[0] == 0:
            continue
        if G[c[0] - 1][c[1]] == "#":
            continue
        c[0] -= 1
    if x == "D":
        if c[0] == H - 1:
            continue
        if G[c[0] + 1][c[1]] == "#":
            continue
        c[0] += 1

c[0] += 1
c[1] += 1

print(*c)
