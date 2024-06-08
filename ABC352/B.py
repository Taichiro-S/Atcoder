S = input()
T = input()

ans = []
start = 0
for s in S:
    found = False
    for i in range(start, len(T)):
        if s == T[i]:
            ans.append(i + 1)
            start = i + 1
            break

print(*ans)
