S = input()

import string

A = list(string.ascii_lowercase)

C = [0] * len(A)

ans = [0] * 100
B = []
for i in range(1, 101):
    for s in S:
        if s not in B:
            ans[S.count(s) - 1] += 1
        B.append(s)

for n in ans:
    if n != 2 and n != 0:
        print("No")
        exit()
print("Yes")
