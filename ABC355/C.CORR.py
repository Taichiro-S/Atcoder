N, T = map(int, input().split())
A = list(map(int, input().split()))

col = [0] * N
row = [0] * N
n = [0] * 2

cnt = 0
bingo = False
for a in A:
    x = (a - 1) // N
    y = (a - 1) % N
    cnt += 1
    row[x] += 1
    col[y] += 1
    if x == y:
        n[0] += 1
        if n[0] == N:
            print(cnt)
            bingo = True
            break
    if x + y == N - 1:
        n[1] += 1
        if n[1] == N:
            print(cnt)
            bingo = True
            break
    if row[x] == N or col[y] == N:
        print(cnt)
        bingo = True
        break

if not bingo:
    print(-1)
