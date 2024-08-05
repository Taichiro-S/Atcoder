N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()

A.sort()


def check(A, n):
    sumA = 0
    for a in A:
        if a < n:
            sumA += a
        else:
            sumA += n
    return M >= sumA


left = -1
right = max(A) + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if check(A, mid):
        left = mid
    else:
        right = mid

print(left)
