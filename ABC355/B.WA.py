N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

for i in range(len(A) - 1):
    if A[i + 1] - A[i] == 1:
        print("Yes")
        exit()

print("No")
