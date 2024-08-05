def hantei(S):
    dep = 0
    for char in S:
        if char == "(":
            dep += 1
        if char == ")":
            dep -= 1
        if dep < 0:
            return False
    return dep == 0


N = int(input())
for i in range(1 << N):
    candidate = ""
    for j in range(N - 1, -1, -1):
        # Note: (i & (1 << j)) == 0 checks if the j-th bit (2^j) of i is 0.
        # This is a bit manipulation technique.
        if (i & (1 << j)) == 0:
            candidate += "("
        else:
            candidate += ")"
    if hantei(candidate):
        print(candidate)

# 自分の回答

N = int(input())

if N % 2 != 0:
    exit()

ans = ["()"]
for i in range(2**N):
    s = ""
    for j in range(N):
        s += "(" if (i >> j) & 1 else ")"
