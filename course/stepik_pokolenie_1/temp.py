# Суммы двух
sum_list = []
temp = 0
for i in range(int(input())):
    if i == 0:
        temp = int(input())
        continue
    cur_number = int(input())
    sum_list.append(cur_number + temp)
    temp = cur_number
print(sum_list)
