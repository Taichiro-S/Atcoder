N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()


s = 0
e = 0

for i in range(K):
    if A[N - 1 - e - 1] - A[s] >= A[N - 1 - e] - A[s + 1]:
        s += 1
    else:
        e += 1

print(A[N - 1 - e] - A[s])
