N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

box = [[] for i in range(N)]

for i in range(N):
    box[A[i] - 1].append(W[i])

box2 = []

for b in box:
    if b != []:
        box2.append(b)

ans = 0
for b in box2:
    b.remove(max(b))
    ans += sum(b)

print(ans)
