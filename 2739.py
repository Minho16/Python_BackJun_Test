N = int(input())
if N<1 or N>9: 
    exit()
else:
    i=1
    for i in range(1,10):
        print(str(N) + " * " + str(i) + " = " + str(N*i))