N = int(input())

P = []

for _ in range(N):
    p = list(map(int, input().split()))
    P.append(p)

ans = -1


for i in range(N):
    if i == 0:
        ans = max(ans, sum([n[0] for n in P[i + 1 :]]) + P[i][1])
    elif i == N - 1:
        ans = max(ans, sum([n[0] for n in P[:i]]) + P[i][1])
    else:
        ans = max(ans, sum([n[0] for n in P[:i] + P[i + 1 :]]) + P[i][1])
print(ans)
