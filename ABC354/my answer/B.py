N = int(input())
S = []
T = 0
for i in range(N):
    s, c = input().split()
    if i == 0:
        S.append(s)
    else:
        flag = False
        for j in range(len(S)):
            if s < S[j]:
                S.insert(j, s)
                flag = True
                break
        if not flag:
            S.append(s)
    T += int(c)

print(S[T % N])
