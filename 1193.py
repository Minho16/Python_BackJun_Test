#무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

#   1/1	1/2	1/3	1/4	1/5	…
#   2/1	2/2	2/3	2/4	…	…
#   3/1	3/2	3/3	…	…	…
#   4/1	4/2	…	…	…	…
#   5/1	…	…	…	…	…
#   …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 
# 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.


X = int(input())

level = 0
list_level = []
i = 1
j = 2
x = 0
y = 0
found = False

while i <= X:
    list_level.append(i)
    i = i+j
    j += 1

if X == 1:
    level = 1
else: 
    level = len(list_level)+1

position = X - list_level[-1]

sum = level + 1

if level == 1:
    x = 1
    y = 1

elif position == 0:
    found = True
    level = level - 1
    sum = sum - 1
    if level % 2 == 0: 
        y = sum - 1
        x = sum - y
    else:
        x = sum - 1
        y = sum - x

if level % 2 == 0 and found == False: 
    x = sum - position
    y = sum - x

elif level % 2 != 0 and found == False and level != 1:
    y = sum - position
    x = sum - y

print(str(y)+"/"+str(x))


