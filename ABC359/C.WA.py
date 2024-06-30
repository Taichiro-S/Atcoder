sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

# if sy>=0 and ty>=0
if sy % 2 == 1 and sx % 2 == 0 and sx > tx:
    sx -= 1
elif sy % 2 == 1 and sx % 2 == 1 and sx < tx:
    sx += 1
elif sy % 2 == 0 and sx % 2 == 1 and sx > tx:
    sx -= 1
elif sy % 2 == 0 and sx % 2 == 0 and sx < tx:
    sx += 1

if ty % 2 == 1 and tx % 2 == 0 and tx > sx:
    tx -= 1
elif ty % 2 == 1 and tx % 2 == 1 and tx < sx:
    tx += 1
elif ty % 2 == 0 and tx % 2 == 1 and tx > sx:
    tx -= 1
elif ty % 2 == 0 and tx % 2 == 0 and tx < sx:
    tx += 1
# elif sx<0 and sy<0:
#     if sy%2==1 and sx%2==0 and sx>tx:
#         sx-=1
#     elif sy%2==1 and sx%2==1 and sx<tx:
#         sx+=1
#     elif sy%2==0 and sx%2==1 and sx>tx:
#         sx-=1
#     elif sy%2==0 and sx%2==0 and sx<tx:
#         sx+=1

#     if sy%2==1 and sx%2==0 and sx>tx:
#         tx-=1
#     elif sy%2==1 and sx%2==1 and sx<tx:
#         tx+=1
#     elif sy%2==0 and sx%2==1 and sx>tx:
#         tx-=1
#     elif sy%2==0 and sx%2==0 and sx<tx:
#         tx+=1
if sx * tx < 0:
    x = abs(tx - sx) + 1
else:
    x = abs(tx - sx)
print(sx, sy, tx, ty)
y = abs(ty - sy)


if x <= y + 1:
    print(y)
else:
    print(x - 1)
