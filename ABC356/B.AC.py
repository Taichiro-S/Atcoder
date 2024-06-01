import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = []
for i in range(N):
    x = list(map(int, input().split()))
    X.append(x)

flag = True

X_rot = np.rot90(X, -1)


for i in range(M):
    if sum(list(X_rot)[i]) < A[i]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
