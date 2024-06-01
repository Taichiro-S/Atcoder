H = int(input())
x = 0
for i in range(100):
    x += 2**i
    if x > H:
        ans = i
        break

print(ans + 1)
