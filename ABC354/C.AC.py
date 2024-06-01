N = int(input())

C = []

for i in range(N):
    a, c = map(int, input().split())
    C.append([a, c, i + 1])

Cs = sorted(C, reverse=True)

ans = [Cs[0]]

for i in range(1, N):
    if ans[-1][1] >= Cs[i][1]:
        ans.append(Cs[i])

ans_s = sorted(ans, key=lambda x: x[2])
ans_i = []
for i in range(len(ans)):
    ans_i.append(ans_s[i][2])

print(len(ans_i))
print(*ans_i)
