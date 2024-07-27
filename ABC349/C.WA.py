S = input()
T = input()

ans = []


def find(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1


if find(S, T[0].lower()) == -1 or find(S, T[1].lower()) == -1:
    print("No")
    exit()

ans.append(find(S, T[0].lower()))

ans.append(find(S[ans[0] + 1 :], T[1].lower()) + ans[0] + 1)

if find(S[ans[1] + 1 :], T[2].lower()) == -1:
    if T[2] == "X":
        print("Yes")
        exit()
    print("No")
    exit()
print("Yes")
