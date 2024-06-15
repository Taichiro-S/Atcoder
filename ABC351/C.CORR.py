n = int(input())
A = list(map(int, input().split()))
a = []
l = 0

for i in range(n):
    a.append(A[i])
    l += 1
    while l > 1:
        if a[l - 2] == a[l - 1]:
            a[l - 2] += 1
            a.pop()
            l -= 1
        else:
            break

print(l)
