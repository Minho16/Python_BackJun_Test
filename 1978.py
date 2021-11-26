N = int(input())
x = list(map(int,input().split()))
count = 0
j = 0

for j in range(N):
   
    num = x[j]
    flag = False

    if num == 1 or num == 0:
        flag = True
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if not flag:
        count = count + 1

print(count)

