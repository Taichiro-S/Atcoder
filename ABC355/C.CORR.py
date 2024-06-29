N,T = map(int,input().split())
A = list(map(int,input().split()))

t = [0]*N
y = [0]*N
n = [0]*2

cnt = 0
bingo = False
for a in A:
    x=(a-1)//N
    y=(a-1)%N
    cnt+=1
    t[x]+=1
    y[y]+=1
    if x==y:
        n[0]+=1
        if n[0]==N:
            print(cnt)
            bingo = True
            break
    if x==y:
        n[0]+=1
        if n[0]==N:
            print(cnt)
            bingo = True
            break
    if t[(a-1)//N]==N or y[(a-1)%N]==N or  or :
        print(cnt)
        bingo = True
        break

if not bingo:
    print(-1)
