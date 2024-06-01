A, B = map(int, input().split())

if A == B:
    print(-1)
    exit()

ans = [1, 2, 3]

ans.remove(A)
ans.remove(B)

print(ans[0])
