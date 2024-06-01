N, L, R = map(int, input().split())

asc = [i for i in range(1, N + 1)]

rev = []

for i in range(L, R + 1):
    rev.append(i)

rev.sort(reverse=True)

ans = asc[0 : L - 1] + rev + asc[R:N]

print(*ans)
