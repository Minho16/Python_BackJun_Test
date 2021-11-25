N = int(input())

A = []
B = []
C = []

for x in range(N):
    a, b = map(int,input().split())
    c = a + b
    A.append(a)
    B.append(b)
    C.append(c)

for x in range(len(A)):
    print(str(C[x]))

