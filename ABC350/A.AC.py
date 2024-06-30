S = input()

n = S[-3:]

ABC = [i for i in range(1, 350) if i != 316]

if int(n) in ABC:
    print("Yes")
else:
    print("No")
