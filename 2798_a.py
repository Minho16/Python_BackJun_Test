# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다

import itertools 

N = 10
M = 500

given_cards = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]


poss_comb_dirty = []

i = 3

while i <= len(given_cards):
    if i == 1:
        for x in given_cards:
            poss_comb_dirty.append(x)
        i += 1
    else:        
        poss_comb_dirty.append((list(itertools.combinations(given_cards,i))))
        i += 1

poss_comb_clean = []
j = 0

while j < len(poss_comb_dirty):
    if type(poss_comb_dirty[j]) == int:
        poss_comb_clean.append(poss_comb_dirty[j])
    else:
        k = 0
        while k < len(poss_comb_dirty[j]):
            poss_comb_clean.append(poss_comb_dirty[j][k])
            k += 1
    j += 1

sum_list = []

for x in poss_comb_clean:
    if type(x) == int:
        sum_list.append(x)
    else:
        l = 0
        sum = 0
        while l < len(x):
            sum = sum + x[l] 
            l += 1
        sum_list.append(sum)

m = 0

closest_number = 0
closest_difference = M
closest_position = 0

while m < len(sum_list):
    if sum_list[m] > M:
        m +=1       
    else:    
        difference = M - sum_list[m]
        if difference < closest_difference:
            closest_difference = difference
            closest_number = sum_list[m]
            closest_position = m
        m += 1

print(sum_list)
print(poss_comb_clean[closest_position])
print(closest_number)
print(closest_difference)
print(closest_position)
