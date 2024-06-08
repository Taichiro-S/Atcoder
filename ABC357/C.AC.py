N = int(input())


def makeCarpet(n):
    newC = []
    if n == 0:
        return [["#"]]
    else:
        C = makeCarpet(n - 1)
        m = int(3 ** (n - 1))
    for i in range(m):
        newC.append(C[i] * 3)
    for i in range(m):
        newC.append(C[i] + ["."] * m + C[i])
    for i in range(m):
        newC.append(C[i] * 3)
    return newC


Cn = makeCarpet(N)

for i in range(3**N):
    print("".join(Cn[i]))
