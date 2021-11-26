N = int(input())
found = False
three_kilo_sugar_count = 0

while found == False:
    five_kilo_sugar_count = N // 5
    five_kilo_sugar_remain = N % 5 
    
    if five_kilo_sugar_remain % 3 == 0:
        three_kilo_sugar_count = five_kilo_sugar_remain // 3
        found = True
    elif five_kilo_sugar_count == 0:
        found = True
    else:
        while five_kilo_sugar_count > 0 and found == False:
            five_kilo_sugar_count = five_kilo_sugar_count - 1
            five_kilo_sugar_remain = five_kilo_sugar_remain + 5

            if five_kilo_sugar_remain % 3 ==0:
                three_kilo_sugar_count = five_kilo_sugar_remain // 3
                found = True
if found == False:
    print(-1)
elif five_kilo_sugar_count + three_kilo_sugar_count == 0:
    print (-1)
else:
    print(five_kilo_sugar_count + three_kilo_sugar_count)

