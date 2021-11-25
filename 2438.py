
N = int(input())
star = "*"

for x in range(N+1):
    if x == 0:
        x += 1
    else:
        print(star * x)
        x += 1
