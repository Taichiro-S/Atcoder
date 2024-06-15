N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())
ans = N
for bit in range(1 << N):
    exist = [False] * M
    visited = 0

    for i in range(N):
        if bit >> i & 1:
            visited += 1
            for j in range(M):
                if S[i][j] == "o":
                    exist[j] = True

    hasAll = True

    for j in range(M):
        if not exist[j]:
            hasAll = False

    if hasAll:
        ans = min(ans, visited)

print(ans)
