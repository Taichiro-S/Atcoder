N, M, K = map(int, input().split())
C, A, R = [], [], []

for _ in range(M):
    CAR = list(input().split())
    C.append(int(CAR[0]))
    A.append(list(map(int, CAR[1:-1])))
    R.append(CAR[-1])

ans = 0
# bit全探索
for mask in range(1 << N):  # 鍵の組み合わせについて
    ok = True  # その組み合わせがテストと矛盾しないかどうか
    for i in range(M):
        cnt = 0
        for a in A[i]:
            # a番目の鍵がテストに含まれていて、
            # 検証中の可能性で正しい鍵かどうか
            cnt += (mask >> (a - 1)) & 1  # maskをa-1ビット右にシフトして1とAND演算

            # テストの結果がOKで、
            # 正しい鍵かどうかを検証中の鍵がK個以上あるか
        ok &= (cnt >= K) == (R[i] == "o")

    ans += ok

print(ans)
