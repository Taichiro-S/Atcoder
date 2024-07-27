N=int(input())
A=list(map(int,input().split()))

pos=[0]*N

for i in range(N):
    pos[A[i]-1] = i+1
print(pos)

for i in range(N):
    