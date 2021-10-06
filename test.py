sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w2_add = input("Give me the number of lemonades sold on the last day of w2")
sales_w2.append(int(sales_w2_add))
sales = sales_w1 + sales_w2
Best_day = max(sales) * 1.5
Worst_day = min(sales) * 1.5 
Total = Best_day + Worst_day

print(Best_day)
print(Worst_day)
print(Total)