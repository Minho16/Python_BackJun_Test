# A: 매년 발생하는 고정비용 (임대료, 재산세, 보험료, 급여 등)
# B: 노트북 1대 생산 비용 (재료비 + 인건비) 

# Example: A = 1000; B = 70 -> 1대 생산 시 1070만원 / 10대 생산 시 1700만원 
# C: 노트북 책정 가격 
# BREAK-EVEN POINT WHEN X*C >= A+(X*B)

# Output => 손익분기점 (X의 값)

import math

A, B, C = map(int,input("Give me the fix cost, production cost per laptop and the selling price: ").split())

if (B>=C):    
    print(str(-1))
else: 
    if (A/(C-B)) - int((A/(C-B))) == 0:  
        print(str(math.ceil(A/(C-B))+1))        
    else:
        print(str(math.ceil(A/(C-B)))) 
        
# 위 문제는 아래와 같이 count로 해결할 경우 시간이 오래 걸림
'''
x = 0

while x <= 2100000000: 
    if x > A/(C-B) and B<C:
        print (x)
        break
    elif (B>C):
        x = -1
        print(x)
        break 
    else: 
        x +=1 
        print(x)
'''

