N = int(input())

P = []

for _ in range(N):
    p = list(map(int, input().split()))
    P.append(p)

ans = -1

a = sum([n[0] for n in P])

for i in range(N):
    ans = max(ans, a - P[i][0] + P[i][1])

print(ans)
