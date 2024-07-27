N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

x, y, nx, ny = 0, 0, 0, 0
xo, yo = False, False
for i in range(N):
    if x > X:
        nx = i
        xo = True
        break
    x += A[i]

for i in range(N):
    if y > Y:
        ny = i
        yo = True
        break
    y += B[i]
if not xo:
    nx = N
if not yo:
    ny = N
print(min(nx, ny))
