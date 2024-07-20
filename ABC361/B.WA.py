a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

if (
    ((a < d and a < g < d) or (a > d and a > g > d))
    and ((b < e and b < h < e) or (b > e and b > h > e))
    and ((c < f and c < i < f) or (c > f and c > i > f))
) or (
    ((a < d and a < j < d) or (a > d and a > j > d))
    and ((b < e and b < k < e) or (b > e and b > k > e))
    and ((c < f and c < l < f) or (c > f and c > l > f))
):
    print("Yes")
else:
    print("No")
