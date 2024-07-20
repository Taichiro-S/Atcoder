xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

a = [xa, ya]
b = [xb, yb]
c = [xc, yc]


def length(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


AB = length(a, b)
BC = length(b, c)
CA = length(c, a)

if AB + BC == CA or AB + CA == BC or CA + BC == AB:
    print("Yes")
else:
    print("No")
