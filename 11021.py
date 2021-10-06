T = int(input())

for i in range(T): 
    x = list(map(int,input().split()))
    print("Case #" + str(i+1) + ": " + str(x[0]+x[1]))
    i += 1