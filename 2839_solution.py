N = int(input())

i = 0

five_kilo_sugar_count = N // 5
five_kilo_sugar_count_list = (list(range(0,five_kilo_sugar_count+1)))
five_kilo_sugar_remain_list = [N-i*5 for i in five_kilo_sugar_count_list]
three_kilo_sugar_count_list = []

for x in five_kilo_sugar_remain_list:
    if x % 3 == 0:
        three_kilo_sugar_count_list.append(x//3)
    else: 
        three_kilo_sugar_count_list.append(10000)

zipped_list = zip(five_kilo_sugar_count_list, three_kilo_sugar_count_list)
sum_list = [x + y for (x,y) in zipped_list]

if sum_list == [] or min(sum_list)>=10000 or min(sum_list) == 0:
    print(-1)
    
else:
    print(min(sum_list))