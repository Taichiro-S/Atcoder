import numpy as np

N, T = map(int, input().split())

A = list(map(int, input().split()))

arr = [[0] * N for i in range(N)]


def is_bingo(l):
    for i in range(N):
        if l[i] == [1] * N:
            return True
    l_90 = np.rot90(l)
    for i in range(N):
        if list(l_90[i]) == [1] * N:
            return True
    if list(np.diag(l)) == [1] * N:
        return True
    if list(np.diag(np.fliplr(l))) == [1] * N:
        return True


ans = 0
for n in A:
    ans += 1
    j = n % N - 1

    if j == -1:
        i = n // N - 1
        j = N - 1
    else:
        i = n // N
    arr[i][j] = 1
    if is_bingo(arr):
        print(ans)
        exit()

print(-1)
