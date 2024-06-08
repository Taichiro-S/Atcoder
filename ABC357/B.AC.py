S = input()
u, l = 0, 0
for s in S:
    if s.islower():
        l += 1
    else:
        u += 1

if l > u:
    print(S.lower())
else:
    print(S.upper())
