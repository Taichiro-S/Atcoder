N, Q = map(int, input().split())
T = list(map(int, input().split()))

tN = [i for i in range(1, N + 1)]

for t in T:
    if t in tN:
        tN.remove(t)
    else:
        tN.append(t)

print(len(tN))
