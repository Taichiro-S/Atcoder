S, T = input().split()

for i in range(1, len(S)):
    l = []
    end = 0
    for j in range(len(S) // i):
        l.append(S[i * j : i * (j + 1)])
        end = max(end, i * (j + 1))
    l.append(S[end:])

    for k in range(i):
        ans = ""
        for j in range(len(l)):
            if k < len(l[j]):
                ans += l[j][k]

        if ans == T:
            print("Yes")
            exit()
print("No")
