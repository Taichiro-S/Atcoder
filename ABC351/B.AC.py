N = int(input())
A, B = [], []
for i in range(N):
    s = input()
    a = []
    for j in range(N):
        a.append(s[j])
    A.append(a)
for i in range(N):
    s = input()
    b = []
    for j in range(N):
        b.append(s[j])
    B.append(b)

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i + 1, j + 1)
