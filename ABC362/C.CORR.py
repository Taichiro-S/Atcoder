N = int(input())
L, R = [], []

for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

if not (sum(L) <= 0 and sum(R) >= 0):
    print("No")
    exit()
print("Yes")
X = L.copy()
sumX = sum(X)
for i in range(N):
    if sumX < 0:
        d = R[i] - L[i]
        s = min(d, -sumX)
        X[i] += s
        sumX += d
    else:
        break
print(*X)
