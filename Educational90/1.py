def solve(M, N, K, L, A):
    cnt = 0
    pre = 0
    for i in range(1, N + 1):
        if A[i] - pre >= M and L - A[i] >= M:
            cnt += 1
            pre = A[i]
    return cnt >= K


N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split()))

left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if not solve(mid, N, K, L, A):
        right = mid
    else:
        left = mid

print(left)
