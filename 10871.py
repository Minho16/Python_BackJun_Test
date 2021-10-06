N,X = map(int,input().split())
A = list(map(int,input().split()))
B = []
for i in A:
    if i<X:
        print(i)
'''print(B)'''
'''
def solution():
    N, X = map(int, input().split())
    
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] < X:
            print(A[i])

solution()
'''