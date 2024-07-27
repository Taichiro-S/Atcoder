N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
minB = 10**10
for i in range(K + 1):
    minB = min(minB, A[N - K + i - 1] - A[i])

print(minB)
