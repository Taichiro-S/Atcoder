N = int(input())
sweet = False
for i in range(N):
    s = input()
    if s == "sweet" and sweet == True:
        if i == N - 1:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

    elif s == "sweet":
        sweet = True
    else:
        sweet = False

print("Yes")
