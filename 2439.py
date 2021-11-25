N = int(input())
star = "*"

for x in range(1,N+1):
    print(" " * (N-x) + star * x)
    x += 1