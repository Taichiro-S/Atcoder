N, K = map(int, input().split())
S = input()

from itertools import permutations

st = set()
for it in permutations(S):
    st.add("".join(it))

cnt = 0

for s in st:
    for i in range(K):
        if s[i : N - K + i + 1] == s[i : N - K + i + 1][::-1]:
            cnt += 1
            break

print(len(st) - cnt)
