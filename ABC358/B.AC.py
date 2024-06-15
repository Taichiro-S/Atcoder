N, A = map(int, input().split())
T = list(map(int, input().split()))
end = 0
for t in T:
    if end > t:
        end += A
        print(end)
    else:
        end = t + A
        print(end)
