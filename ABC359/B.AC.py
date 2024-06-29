N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(2, 2 * N):
    if A[i] == A[i - 2]:
        cnt += 1

print(cnt)
