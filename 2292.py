N = int(input())
circle = 1

while N >= 0:
    if circle == 1: 
        N = N - 1 
        circle += 1 
    else: 
        if N == 0:
            break       
        else: 
            N = N-((circle-1)*6)
            circle += 1     
print(circle-1)